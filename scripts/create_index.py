from typing import List, Tuple
import os
import json
from run_completion import run_completion
from datetime import datetime

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

prompt_version = '1'

def create_file_description(file_path: str, rel_path: str, url: str, index: List[dict]) -> Tuple[List[dict], int, int]:
    # make a copy of the index
    index = index.copy()
    # find existing description
    index_entry = next((entry for entry in index if entry['path'] == rel_path), None)
    if index_entry:
        if index_entry.get('prompt_version') == prompt_version:
            # Skip if the description already exists
            print(f"Skipping {file_path} - description already exists")
            return index, 0, 0
        else:
            print(f"Updating {file_path} - description exists with different prompt version")
            index = [
                entry for entry in index if entry['path'] != rel_path
            ]

    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    print(f"Processing {file_path}")

    # Read system message
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'system_message.txt'), 'r', encoding='utf-8') as f:
        system_message = f.read().strip()

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": file_content}
    ]

    model = 'anthropic/claude-3.7-sonnet'

    # Get the completion
    response, _, prompt_tokens, completion_tokens = run_completion(
        messages=messages,
        model=model
    )

    print(f"Tokens used - Prompt: {prompt_tokens}, Completion: {completion_tokens}")

    index.append({
        'path': rel_path,
        'url': url,
        'description': response,
        'model': model,
        'prompt_tokens': prompt_tokens,
        'completion_tokens': completion_tokens,
        'timestamp': datetime.now().isoformat(),
        'prompt_version': prompt_version
    })
    # sort the index by path
    index.sort(key=lambda x: x['path'])
    return index, prompt_tokens, completion_tokens

def main(mode: str):
    # Track total token usage
    total_prompt_tokens = 0
    total_completion_tokens = 0
    files_processed = 0

    index_json_path = 'index.json'

    if os.path.exists(index_json_path):
        with open(index_json_path, 'r', encoding='utf-8') as f:
            index = json.load(f)
    else:
        index = []

    # Walk through the docs directory
    if mode == 'pynwb':
        docs_gallery_path = 'submodules/pynwb/docs/gallery'
    elif mode == 'neuroconv_conversion_examples_gallery':
        docs_gallery_path = 'submodules/neuroconv/docs/conversion_examples_gallery'
    elif mode == 'neuroconv_user_guide':
        docs_gallery_path = 'submodules/neuroconv/docs/user_guide'
    elif mode == 'nwbinspector':
        docs_gallery_path = 'submodules/nwbinspector/docs/best_practices'
    elif mode == 'hdmf':
        docs_gallery_path = 'submodules/hdmf/docs/gallery'
    else:
        raise ValueError("Invalid mode.")
    for root, _, files in os.walk(docs_gallery_path):
        for file in files:
            if mode.startswith('neuroconv') or mode.startswith('nwbinspector'):
                ext = '.rst'
            else:
                ext = '.py'
            if file == 'index.py' or file == 'index.rst':
                # Skip index files
                continue
            if file.endswith(ext):
                file_path = os.path.join(root, file)
                assert file_path.startswith('submodules/')
                rel_path = file_path[len('submodules/'):]
                if mode == 'pynwb':
                    # submodules/pynwb/docs/gallery/domain/ecephys.py
                    # goes to
                    # https://pynwb.readthedocs.io/en/latest/tutorials/domain/ecephys.html
                    url = f"https://pynwb.readthedocs.io/en/latest/tutorials/{rel_path[len('pynwb/docs/gallery/'):-3]}.html"
                elif mode == 'neuroconv_conversion_examples_gallery':
                    # submodules/neuroconv/docs/conversion_examples_gallery/recording/intan.rst
                    # goes to
                    # https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/intan.html
                    url = f"https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/{rel_path[len('neuroconv/docs/conversion_examples_gallery/'):-4]}.html"
                elif mode == 'neuroconv_user_guide':
                    # submodules/neuroconv/docs/user_guide/csvs.rst
                    # goes to
                    # https://neuroconv.readthedocs.io/en/main/user_guide/csvs.html
                    url = f"https://neuroconv.readthedocs.io/en/main/user_guide/{rel_path[len('neuroconv/docs/user_guide/'):-4]}.html"
                elif mode == 'nwbinspector':
                    # submodules/nwbinspector/docs/best_practices/nwbfile_metadata.py
                    # goes to
                    # https://nwbinspector.readthedocs.io/en/dev/best_practices/nwbfile_metadata.html
                    url = f"https://nwbinspector.readthedocs.io/en/dev/best_practices/{rel_path[len('nwbinspector/docs/best_practices/'):-4]}.html"
                elif mode == 'hdmf':
                    # submodules/hdmf/docs/gallery/plot_aligneddynamictable.py
                    # goes to
                    # https://hdmf.readthedocs.io/en/stable/tutorials/plot_aligneddynamictable.html
                    url = f"https://hdmf.readthedocs.io/en/stable/tutorials/{rel_path[len('hdmf/docs/gallery/'):-3]}.html"
                else:
                    raise ValueError("Invalid mode.")
                try:
                    index, p_tokens, c_tokens = create_file_description(file_path, rel_path, url, index)
                    total_prompt_tokens += p_tokens
                    total_completion_tokens += c_tokens
                    files_processed += 1
                    with open(index_json_path, 'w', encoding='utf-8') as f:
                        json.dump(index, f, indent=4)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    raise
                    # continue

    print("\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Total tokens used - Prompt: {total_prompt_tokens}, Completion: {total_completion_tokens}")

    # Generate index.md with urls and descriptions
    print("Generating index.md...")
    with open('index.md', 'w', encoding='utf-8') as f:
        for entry in index:
            f.write(f"{entry['url']}\n\n")
            f.write(f"{entry['description']}\n")
            f.write("\n---\n\n")

if __name__ == "__main__":
    main('pynwb')
    main('neuroconv_conversion_examples_gallery')
    main('neuroconv_user_guide')
    main('nwbinspector')
    main('hdmf')
