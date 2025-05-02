https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/audio.html

The document explains how to convert audio data from WAV format to NWB format using NeuroConv's AudioInterface class, including installation instructions, sample code for executing a conversion, and steps for adding metadata such as session start time.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/deeplabcut.html

The document describes how to convert DeepLabCut pose estimation data to NWB format using NeuroConv, including installation instructions and sample Python code demonstrating the conversion process with the DeepLabCutInterface class.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/fictrac.html

This document explains how to convert FicTrac behavioral data (spherical motion and fictive animal path) to the NWB (Neurodata Without Borders) format using the NeuroConv Python package, providing installation instructions and code examples for the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/lightningpose.html

This document explains how to convert LightningPose pose estimation data to NWB format using the NeuroConv package, showing how to install dependencies and use the LightningPoseConverter with sample code for loading data files, setting metadata, and executing the conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/medpc.html

A guide for converting MedPC operant behavior data (like nose pokes and rewards) to NWB format using the NeuroConv Python package, including code examples for installation, data interface setup, metadata extraction, and file conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/neuralynx_nvt.html

The document explains how to convert Neuralynx NVT position tracking data to Neurodata Without Borders (NWB) format using the NeuralynxNvtInterface from the NeuroConv package, including installation instructions and a code example for the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/sleap.html

A guide on converting SLEAP pose estimation data to NWB format using NeuroConv's SLEAPInterface, including installation instructions and a Python code example showing how to extract metadata, set required parameters, and run the conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/behavior/video.html

The document explains how to convert video data to NWB format using NeuroConv, covering both external storage (ExternalVideoInterface) and internal storage (InternalVideoInterface) approaches. It includes code examples for installation, basic conversion, and proper metadata specification for each method, with recommendations based on whether videos contain natural behavior or neural data.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/combinations/ecephys_pose_estimation.html

This example demonstrates how to combine electrophysiology (using BlackrockRecordingInterface and KiloSortSortingInterface) and behavioral data (using SLEAPInterface for pose estimation) into a single NWB file using the ConverterPipe class from NeuroCONV.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/combinations/spikeglx_and_phy.html

This document outlines a workflow for combining electrophysiology recordings from SpikeGLX with spike sorting data from Phy using NeuroConv's conversion tools, including code examples that demonstrate how to create interface objects, extract metadata, and run the conversion to NWB format.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/combinations/tiff_and_suite2p.html

A code example demonstrating how to use NeuroConv to convert optical physiology data from Tiff imaging files processed with Suite2p segmentation algorithm into NWB format, showing the workflow for combining imaging data with segmentation results using TiffImagingInterface and Suite2pSegmentationInterface classes.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/conftes.html

A pytest configuration file that sets up fixtures for doctests by providing data paths, creates temporary paths for test output, and conditionally skips certain doctests based on Python version and operating system (particularly for deeplabcut.rst on Python 3.9/macOS and sleap.rst tests with specific ndx-pose versions).

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/fiberphotometry/tdt_fp.html

A guide for converting TDT Fiber Photometry data to NWB format using NeuroConv, including detailed metadata specification for optical fibers, excitation sources, photodetectors, filters, indicators, and instructions for running the conversion with sample Python code.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/brukertiff.html

This document explains how to convert Bruker TIFF imaging data to NWB format using NeuroConv, showing examples for both single plane conversion (BrukerTiffSinglePlaneConverter) and multi-plane/volumetric imaging data (BrukerTiffMultiPlaneConverter) with code snippets for installation and implementation.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/hdf5imaging.html

This document provides instructions for converting HDF5 imaging data to NWB format using the NeuroConv library, including how to install the necessary dependencies and sample Python code for performing the conversion with the Hdf5ImagingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/image.html

The document describes the ImageInterface in NeuroConv for converting various image formats (PNG, JPG, TIFF) to NWB format, including supported image modes, example usage, and key features such as memory efficiency, automatic mode conversion, multiple input methods, and options for storing images in acquisition or stimulus groups.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/micromanagertiff.html

This document explains how to use NeuroConv to convert Micro-Manager TIFF imaging data to NWB format, including installation instructions and Python code examples that demonstrate the conversion process using the MicroManagerTiffImagingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/miniscope.html

The document explains how to convert Miniscope data (which records optical physiology and behavior as video data) to NWB format using the NeuroConv library, including installation instructions and Python code examples showing how to use the MiniscopeConverter class to combine recording and behavioral data streams into a single NWB file.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/scanbox.html

This document explains how to convert Scanbox imaging data to NWB format using the NeuroConv Python package, including installation instructions and a code example demonstrating the SbxImagingInterface conversion workflow.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/scanimage.html

A guide for converting ScanImage imaging data to NWB format using NeuroConv, covering single and multi-plane imaging data from both single files and multiple buffered files with code examples for each conversion scenario.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/thor.html

This document explains how to convert Thor TIFF imaging data to NWB format using the ThorImagingInterface from NeuroConv, including installation instructions and a code example showing the conversion process for data acquired with ThorImageLS software.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/imaging/tiff.html

A guide for converting TIFF imaging data to NWB format using NeuroConv's TiffImagingInterface, including installation instructions and Python code example for handling multi-page TIFF files with metadata specification.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/index.html

This document is a conversion gallery for the NeuroConv library, listing supported data formats for various neuroscience data types including extracellular/intracellular electrophysiology, optical physiology, behavior tracking, and common file formats, with links to specific documentation for each converter.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/abf.html

A guide for converting ABF (Axon Binary Format) intracellular electrophysiology data to NWB (Neurodata Without Borders) format using NeuroConv, with examples of both single and multiple ABF file conversions including metadata assignment.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/alphaomega.html

This document provides instructions for converting AlphaOmega electrophysiology data to the NWB (Neuro Data Without Borders) format using the NeuroConv package, including installation commands and Python code examples for the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/axona.html

The document provides instructions for converting Axona electrophysiology data to NWB format using NeuroConv, including code examples for installing the required packages, initializing the AxonaRecordingInterface with a .bin file, extracting metadata, and executing the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/biocam.html

The document outlines the process for converting Biocam electrophysiology data to Neurodata Without Borders (NWB) format using NeuroConv, including installation instructions with required dependencies and a Python code example demonstrating the conversion workflow with the BiocamRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/blackrock.html

This document provides instructions for converting Blackrock/Ripple Neuro neurophysiological data to the NWB (Neurodata Without Borders) format using the NeuroConv Python package, including code examples for installation and implementation of the BlackrockRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/edf.html

The document explains how to convert European Data Format (EDF) files to Neurodata Without Borders (NWB) format using the NeuroConv package, including installation instructions, code examples for implementing the EDFRecordingInterface, and how to extract and add metadata during conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/intan.html

The document provides instructions for converting Intan electrophysiology data to Neurodata Without Borders (NWB) format using NeuroConv, including code examples showing the installation process and conversion steps with the IntanRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/maxone.html

This document explains how to convert MaxOne electrophysiology data to the NWB format using NeuroConv, including installation instructions, code examples, and essential metadata configuration for proper data conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/mcsraw.html

The document provides instructions for converting MCSRaw electrophysiology data to NWB format using NeuroConv, including installation commands with required dependencies and a Python code example that demonstrates the conversion process with the MCSRawRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/mearec.html

This document explains how to convert MEArec electrophysiology data to the Neurodata Without Borders (NWB) format using NeuroConv, including installation instructions and a Python code example that demonstrates creating a MEArecRecordingInterface, extracting metadata, and running the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/neuralynx.html

This document provides instructions for converting Neuralynx electrophysiology data to NWB format using NeuroConv, including code examples for installation, metadata extraction, and running the conversion process with the NeuralynxRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/neuroscope.html

This document provides instructions for converting NeuroScope electrophysiology data to NWB format using the NeuroConv Python package, including installation steps and a code example demonstrating how to use the NeuroScopeRecordingInterface to perform the conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/openephys.html

This document explains how to convert OpenEphys electrophysiology data to the NWB (Neurodata Without Borders) format using the NeuroConv Python package, including installation instructions and a code example demonstrating the conversion process with the OpenEphysRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/plexon.html

The document explains how to convert Plexon recording data to NWB format using NeuroConv, including installation instructions, code examples for using the PlexonRecordingInterface, and steps for extracting metadata and running the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/plexon2.html

This document explains how to convert Plexon2 recording data to NWB format using the NeuroConv Python package, including installation instructions, a warning about non-Windows platforms requiring wine, and code examples showing how to initialize the interface, extract metadata, and run the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/spike2.html

The document provides instructions for converting Spike2 electrophysiology data to Neurodata Without Borders (NWB) format using the NeuroConv Python package, including code examples for installation and the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/spikegadgets.html

This guide explains how to install NeuroConv with Spikegadgets dependencies and convert Spikegadgets neurophysiology data to the NWB format using the SpikeGadgetsRecordingInterface, including code examples for installation, metadata extraction, and file conversion.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/spikeglx.html

This document explains how to convert SpikeGLX electrophysiology data to NWB format using NeuroConv, including methods for converting entire SpikeGLX folder structures with SpikeGLXConverterPipe or individual data streams (AP/LF) with SpikeGLXRecordingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/recording/tdt.html

The document explains how to convert Tucker-Davis Technologies (TDT) data to NWB format using NeuroConv, providing installation instructions and sample Python code that demonstrates creating a TdtRecordingInterface instance, extracting metadata, and running the data conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/segmentation/caiman.html

This document explains how to convert CaImAn segmentation data to NWB format using NeuroConv's CaimanSegmentationInterface, providing installation instructions and a code example with metadata configuration for the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/segmentation/cnmfe.html

A guide for installing NeuroConv with CNMF-E dependencies and converting CNMF-E segmentation data to NWB format using the CnmfeSegmentationInterface, including sample code for initialization, metadata setup, and running the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/segmentation/extract.html

A guide for converting EXTRACT segmentation data to NWB format using NeuroConv's ExtractSegmentationInterface, including installation instructions with additional dependencies and Python code example demonstrating the conversion process with metadata handling.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/segmentation/suite2p.html

This document explains how to convert suite2p segmentation data to NWB format using NeuroConv, including installation instructions, basic usage of Suite2pSegmentationInterface with code examples, and guidance for handling multiple planes and channels from the same dataset.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/blackrock.html

The document describes how to convert Blackrock sorting data to NWB format using NeuroConv, providing installation instructions and Python code examples with the BlackrockSortingInterface class to extract metadata and run the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/cellexplorer.html

A guide for converting CellExplorer neural recording data to NWB format using NeuroConv's CellExplorerSortingInterface, including installation instructions and Python code examples for the conversion process.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/kilosort.html

The document explains how to convert KiloSort spike-sorting data to the NWB (Neurodata Without Borders) format using the NeuroConv package, including installation instructions and a Python code example demonstrating the conversion process with the KiloSortSortingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/neuralynx.html

This guide explains how to convert Neuralynx data to NWB format using the NeuroConv package, including installation steps with required dependencies and a Python code example demonstrating the conversion process with the NeuralynxSortingInterface.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/neuroscope.html

This document explains how to convert NeuroScope sorting data to NWB format using NeuroConv, showing installation instructions and Python code for using the NeuroScopeSortingInterface to perform the conversion with required parameters.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/phy.html

This document explains how to convert Phy sorting data to the NWB format using the PhySortingInterface from NeuroConv, including installation instructions with pip and a Python code example demonstrating the conversion process with metadata configuration.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/sorting/plexon.html

The document provides instructions for converting Plexon spiking data (.plx) files to Neurodata Without Borders (NWB) format using the PlexonSortingInterface from the NeuroConv package, including code examples for installation and data conversion with metadata handling.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/text/csv.html

A guide for converting CSV files to NWB format using NeuroConv's CsvTimeIntervalsInterface, with code examples showing how to properly install the package, read CSV files containing time interval data, and convert them to trials in an NWB file.

---

https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/text/excel.html

A guide for converting Excel data to Neurodata Without Borders (NWB) format using the ExcelTimeIntervalsInterface from NeuroConv, including installation instructions, code examples for reading Excel files with time interval data, and steps for properly configuring metadata.

---

https://neuroconv.readthedocs.io/en/main/user_guide/adding_trials.html

The document explains how to add trial timing information to NWB files using PyNWB, including adding custom columns to trials tables, adding trial entries with specific parameters, and saving the NWB file to disk with optimized storage settings.

---

https://neuroconv.readthedocs.io/en/main/user_guide/aws_demo.html

The document outlines how to deploy NWB data conversions in AWS cloud services using NeuroConv's AWS tools. It provides a detailed tutorial on setting up a pipeline that transfers source data from cloud storage to AWS, performs NWB conversion, and uploads results to the Dandi Archive, covering prerequisites like Google Drive setup, Rclone configuration, AWS account access, and the steps to create and deploy an AWS Batch job for neurophysiology data conversion.

---

https://neuroconv.readthedocs.io/en/main/user_guide/backend_configuration.html

The document explains how to configure backend file storage in NeuroConv, including controlling chunking, compression, and buffering patterns for NWB files. It covers retrieving default configurations, customizing dataset configurations, and applying them when writing NWB files through DataInterfaces or Converters, with examples showing how to modify compression methods and other parameters.

---

https://neuroconv.readthedocs.io/en/main/user_guide/csvs.html

This document describes how to specify metadata using tabular formats (CSV files) in the NeurConv library, showing example CSV file structures for sessions and subjects, and providing Python code to read the CSV files, process the data, and convert it to NWB format using SpikeGLXRecordingInterface and DeepLabCutInterface.

---

https://neuroconv.readthedocs.io/en/main/user_guide/datainterfaces.html

The document describes the BaseDataInterface class in NeuroConv, which provides a unified API for converting data into NWB format, covering its installation with specific dependencies, initialization with source data, extraction and adjustment of metadata, and running the conversion process either directly to a file or by creating an in-memory NWB file that can be modified before saving.

---

https://neuroconv.readthedocs.io/en/main/user_guide/docker_demo.html

The document demonstrates how to use NeuroConv's Docker implementation to convert neurophysiology data to NWB format using YAML specifications. It walks through a complete example showing how to set up directories, create a YAML configuration file, and run the Docker container with proper volume mounting to convert SpikeGLX and Phy data. The second section explains how to use NeuroConv's Rclone Docker image for data transfers between remote storage systems and local directories.

---

https://neuroconv.readthedocs.io/en/main/user_guide/expand_path.html

The document describes the path expansion tools in NeuroConv that allow users to identify data files and extract metadata from their file paths. It explains how to use LocalPathExpander to match file patterns and automatically extract metadata like subject IDs and session timestamps from organized directory structures, with examples from real datasets including Allen Institute, Buszaki Lab, and IBL Brain Wide Map data.

---

https://neuroconv.readthedocs.io/en/main/user_guide/index.html

NeuroConv is a tool for converting neurophysiology experiment data to NWB format, using DataInterface classes to handle specific data formats and a NWBConverter class to combine multiple data sources into a unified conversion with synchronization capabilities.

---

https://neuroconv.readthedocs.io/en/main/user_guide/linking_sorted_data.html

This document explains how the SortedRecordingConverter maintains proper linkage between sorted neural units and recording electrodes in NWB files by creating electrode table regions, maintaining device relationships, and correctly mapping channel IDs to electrode indices, with examples demonstrating its usage for single-probe recordings.

---

https://neuroconv.readthedocs.io/en/main/user_guide/nwbconverter.html

NWBConverter is a Python class that simplifies converting multiple neurophysiological data sources with different proprietary formats into a single NWB file, allowing users to combine data interfaces (like SpikeGLXRecording and PhySorting), specify metadata, and control conversion options for each interface.

---

https://neuroconv.readthedocs.io/en/main/user_guide/temporal_alignment.html

The document explains temporal alignment methods in NeuroConv for synchronizing data across multiple acquisition systems in neurophysiology experiments. It covers three synchronization approaches: 1) aligning start times for simple offset correction, 2) synchronizing timestamps using signals at every sample to correct for drift, and 3) using regular synchronization signals with interpolation. It includes details on extracting TTL pulse signals and implementing temporal alignment within the NWBConverter framework, with code examples for each method.

---

https://neuroconv.readthedocs.io/en/main/user_guide/yaml.html

This document explains how to use YAML files to specify metadata for NWB conversions, showing the format for NWBFile and Subject metadata, indicating required fields, and demonstrating how to incorporate YAML metadata into Python conversion pipelines using NeuroConv's utilities.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/h5dataio.html

This document explains how to customize HDF5 dataset I/O settings in PyNWB, including chunking, compression, and filters, using the H5DataIO wrapper to optimize storage and performance while maintaining backend independence.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/parallelio.html

This tutorial explains how to use parallel I/O with MPI in PyNWB, covering how to instantiate datasets for parallel writing, write to NWB files in parallel using MPI, and read from NWB files in parallel, with code examples demonstrating the process using mpi4py, NWBHDF5IO, and H5DataIO.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/plot_editing.html

The document explains how to edit NWB files in-place, covering techniques for modifying datasets (changing values, attributes, and shapes), renaming groups, and adding new datasets to existing groups, with examples showing how to use PyNWB and h5py to make these edits while maintaining file validity.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/plot_iterative_write.html

A tutorial on iterative data writing in PyNWB, covering techniques for efficiently handling large data arrays, streaming data, and sparse arrays without loading everything into memory at once.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/plot_linking_data.html

This document explains how to link and store data across multiple files in PyNWB, showing methods for external linking to datasets or containers from separate NWB files, copying NWBFiles with links to original data, consolidating linked files for sharing, and automatically splitting large datasets across multiple files using the HDF5 family driver.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/plot_zarr_io.html

The document explains how to use Zarr as an alternative backend for NWB (Neurodata Without Borders) files, highlighting its advantages for large datasets and cloud storage, and demonstrating how to configure datasets with compression, write NWB files to Zarr format, and read them back using the hdmf-zarr package.

---

https://pynwb.readthedocs.io/en/latest/tutorials/advanced_io/streaming.html

Summary of methods for streaming NWB files from remote sources, particularly DANDI Archive. The document explains three approaches: using remfile (a lightweight, fast library optimized for HDF5), fsspec (a flexible virtual filesystem solution), and ROS3 driver in h5py (requires special installation), with code examples showing how to retrieve and access data from each method.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/ecephys.html

This document is a tutorial on storing extracellular electrophysiology data in NWB format using PyNWB, covering the creation of electrode tables, adding raw voltage data, LFP data, and spike data. It demonstrates how to create NWB files, define electrode groups and devices, store different types of neural recordings, and handle both sorted and unsorted spike times, with code examples for writing and reading the data.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/images.html

The document provides a tutorial on storing image data in NWB (Neuro Data Without Borders) format using PyNWB, demonstrating how to add various types of image data including OpticalSeries for stimuli presentation, ImageSeries for acquisition data, static images (RGB/RGBA/Grayscale), and IndexSeries for efficient storage of repeated images, along with code examples for writing and reading these image datasets.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/ogen.html

This tutorial demonstrates how to create and write optogenetics data to an NWB (Neurodata Without Borders) file, including how to add devices, stimulus sites (OptogeneticStimulusSite), and time series data (OptogeneticSeries) with proper metadata.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/ophys.html

This document provides a comprehensive tutorial on writing calcium imaging data to NWB files, covering the creation of imaging planes, adding two-photon images, implementing motion correction, adding image segmentation with ROI definitions, and storing fluorescence responses with code examples for writing and reading NWB files.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/plot_behavior.html

The tutorial explains how to add behavioral data to an NWBFile using the pynwb.behavior module, covering how to store continuous position data, view angles, behavioral time series, events, and epochs, as well as eye-tracking data, with examples of creating, writing, and reading specific behavior data types.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/plot_icephys.html

This document explains storage of intracellular electrophysiology data in NWB (Neurodata Without Borders) format, covering TimeSeries data types, metadata organization in hierarchical tables, and the process of creating and populating NWB files with electrophysiology recordings, stimuli, and experimental conditions.

---

https://pynwb.readthedocs.io/en/latest/tutorials/domain/plot_icephys_pandas.html

The document is a tutorial on using pandas to query intracellular electrophysiology metadata in NWB (Neurodata Without Borders) files, demonstrating how to convert hierarchical metadata tables into pandas DataFrames, access related tables, and perform common metadata queries on experimental conditions, recordings, stimuli, and responses.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/add_remove_containers.html

The document provides a tutorial on adding and removing containers from NWB files using PyNWB, explaining two main approaches: modifying files in read/write mode, and exporting data to new files with the ability to add or remove components.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/extensions.html

This document provides a tutorial on extending the Neurodata Without Borders (NWB) format, explaining how to create, document, and use Neurodata Extensions (NDX), including creating custom data types, caching extensions, implementing MultiContainerInterface, and working with specialized data structures like cortical surface meshes.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/object_id.html

The document explains how to work with object IDs in NWB (Neurodata Without Borders) files, showing how every NWB container has a UUID string identifier that can be accessed via the object_id method and how these IDs can be used to retrieve objects from an NWBFile's objects dictionary.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/plot_configurator.html

A guide explaining how to use configuration files in PyNWB to validate specific fields against allowed term sets, including how to create, load, and unload configuration files, with examples showing the validation of "experimenter" and "species" fields in NWBFile and Subject classes.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/plot_file.html

The document provides a comprehensive overview of working with NWB (Neurodata Without Borders) files in Python, including creating and manipulating files, storing time series data, adding subject information, handling spatial position data, organizing data in processing modules, and reading/writing/appending to NWB files.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/plot_read_basics.html

This document explains how to read and explore NWB (Neurodata Without Borders) files using Python, covering how to download neurophysiology data from DANDI archive, access the file contents including stimulus data, single unit recordings, and trial information, and visualize neural activity and stimuli with basic plots.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/plot_timeintervals.html

The document explains how to annotate time intervals in neuroscience data using NWB's TimeIntervals structure, detailing methods for creating, accessing, and storing trials, epochs, and custom time intervals with TimeSeries references, including code examples for defining intervals and linking them to specific data ranges.

---

https://pynwb.readthedocs.io/en/latest/tutorials/general/scratch.html

A tutorial on using PyNWB's scratch space for storing exploratory or non-standardized analysis results, demonstrating how to copy NWB files, add processed data to processing modules, and use scratch space for storing intermediate analyses that don't require formal extensions.

---

