## [Challenge 12](https://github.com/ECMWFCode4Earth/challenges_2023/issues/3) – Compression of Geospatial Data with Varying Information Density ([Link to G-Doc](https://docs.google.com/document/d/1FD5dQIBb9xBYCU9RIoggPZZV_C3qqEwmdCTHJbM3VZ4/edit?usp=sharing))

[Code for Earth / Innovation - Collaboration](https://codeforearth.ecmwf.int/) 


## 1. Background / Motivation

As a brief introduction, I would describe myself as a curious, creative, disciplined, and collaborative individual who possesses a keen interest in remote sensing, machine learning, image processing, and 3D computer vision. I am naturally inclined towards troubleshooting and overcoming obstacles, and I am an experienced Python user. During the summer of 2021, I gained hands-on experience in integrating a 3D scanning module to create a building model using images captured by the MapMint4ME Android application and visualizing it on MapMint. Additionally, for my master's thesis, I worked on the project of  "Localization, back-projection, and fusion of LWIR hyperspectral data from FTIR imaging sensors".

As a graduate in Geomatics and Surveying engineering, I have always been fascinated by the vast amounts of geospatial data available and its potential applications in various fields. However, the challenge of handling and storing such large datasets has always been a concern, especially in countries with limited computational resources, such as my home country, Morocco.

Technological advancements and increased computing power have led to the rapid expansion of geospatial data, resulting in the generation of massive, high-resolution datasets that are essential for climate modeling, environmental monitoring, and oceanic and atmospheric research. These large datasets pose challenges in terms of storage, management, and analysis, necessitating efficient compression techniques.

Although the xbitinfo package offers a promising open-source solution for lossy compression of geospatial data, its current implementation does not fully exploit the spatial and temporal variability that is common in most geospatial datasets. This variability is driven by changes in the information density of the data in both space and time. For example, a snow precipitation dataset may exhibit significant variability in different parts of the world, with some regions experiencing heavy snowfall and others little to none at all. Additionally, the same location may have different levels of snowfall depending on the season. By exploiting this variability, the compression performance can be improved and more efficient storage and analysis of geospatial data can be achieved.

I am excited to present this proposal, which aims to enhance xbitinfo's capabilities, optimize its compression performance, and ensure accurate and efficient handling of complex geospatial data. My motivation for this project stems from a deep interest in the intersection of Earth data science and software engineering, and a desire to apply my technical skills to solve real-world problems.


## 2. Challenge 

Geospatial data exhibits significant variability in information density both spatially and temporally. This variability poses a challenge for existing compression techniques, as they struggle to preserve the rich information content in regions with high density while discarding random noise in areas with low density.

xbitinfo's current framework, which relies on maximum information content for the entire dataset, leads to suboptimal compression performance. To overcome these limitations, the project will focus on refining xbitinfo's approach to leverage the inherent spatial and temporal variability of geospatial data. This will enable more efficient data storage and analysis.


## 3. The proposed solution

A multi-resolution compression solution will be investigated and implemented to address the identified challenge. It consists of developing a multi-resolution compression algorithm that recognizes and adapts to varying information density across the dataset. This approach can either be implemented in a static or a dynamic way and will ensure optimal compression performance without compromising the fidelity of information-rich regions. A combination of some of the following ideas will be explored to this end:

A. Identification of the adaptive compression technique of geospatial data with xbitinfo:
1. Spatial and temporal chunk-based analysis: Extend xbitinfo’s current methodology to include both spatial and temporal chunk-based bit information calculation. Study the optimal chunk size to consider depending on the feature effective scale.  \
This approach involves dividing the geospatial dataset into fixed-sized chunks or blocks, with each block having a predetermined size (e.g., every 512x512 values) and time period (e.g., every T period). The bit information content is then calculated for each chunk, taking into account the variability in information density within each block. 
[**Optional**: dynamic chunk size identification can be explored if the static method is completed]

2. Combination of lossy and lossless compression techniques: Use a combination of lossy and lossless compression techniques to optimize the compression ratio while maintaining data quality. Lossy can be used to compress parts of the dataset that contain little information while using lossless compression techniques in locations with high information density. 
3. Machine learning-assisted compression: 
    1. Unsupervised clustering algorithm: Analyze the geospatial data and identify areas of high and low information density. 
    2. Deep-learning based compression: Explore the potential of deep-learning techniques such as convolutional neural networks and autoencoders, for predicting the optimal chunk size based on the local information of geospatial features. 
    3. Adaptive Wavelet transform: Explore the potential of adaptive wavelet transform techniques that dynamically adjust the compression parameters based on information density in both spatial and temporal domains. 
    4. Graph-based compression: Investigate the application of graph-based compression methods for encoding the spatial and temporal correlation in-geospatial data. 

B. Seamless integration and compatibility: Ensure that the improved xbitinfo package integrates seamlessly with the existing Pangeo ecosystem and remains compatible with xarray, dask, netCDF, and zarr data formats. Another option could be to ensure that the improved xbitinfo package integrates seamlessly with cloud-based data storage and processing systems.

C. Evaluation and comparison with state-of-the-art techniques: Perform extensive benchmarking and validation of the updated xbitinfo package, comparing its performance against the original implementation and other state-of-the-art compression techniques. 


## 4. Key milestones and deliverables

* Milestone 1: Research and development 
    * Deliverable 1.1: Comprehensive literature review of recent advancements in data compression techniques, focusing on adaptive algorithms that can be applied to spatial and temporal chunks of geospatial data, and on methods used on the binary representations of the data.
    * Gain familiarity with dask and zarr
* Milestone 2: Design and implementation
    * Deliverable 2.1: Design and development of an adaptive compression algorithm for xbitinfo that adjusts compression parameters based on local information density in spatial and temporal chunks.
    * Deliverable 2.2: Implementation of machine learning-based compression techniques, such as deep learning, for predicting and adapting to the spatial and temporal variability of information density within data chunks.
* Milestone 3: Integration and compatibility
    * Deliverable 3.1: Seamless integration of the improved xbitinfo package with the existing Pangeo ecosystem, ensuring compatibility with xarray, dask, netCDF, and zarr data formats.
* Milestone 4: Evaluation and benchmarking
    * Deliverable 4.1: Comprehensive benchmarking and validation of the updated xbitinfo package using chunk-based compression, comparing its performance against the original implementation and other state-of-the-art compression techniques.
* Milestone 5: Documentation and dissemination
    * Deliverable 5.1: Comprehensive user documentation and API reference for the updated xbitinfo package, focusing on the new chunk-based processing and compression capabilities.
    * Deliverable 5.2: Presentation of project findings at ECMWF-Bologna and publication of results in a peer-reviewed journal or workshop at a top AI conference. 


## 5. Proposed Timeline

[Link to G-Sheet](https://docs.google.com/spreadsheets/d/1yxded_C6VJ5N5cQETiBNVlD0Es4fBzNRK7gzDeuUMu4/edit?usp=sharing)

|               | May           | June  | July  | August|
| ------------- |:-------------:|:-----:|:-----:|:-----:|
| Research and developments      | O | O |   |   |
| Design of compression algoritm      |  | O | O |   |
| Implementation of ml-based compression   |   | O | O |   |
| Integration and compatibility      |   | O | O |   |
| Evaluation and benchmarking    |  |  | O | O |
| Documentation      |  |  |   | O |
| Dessemination      |   |   |  | O |


## 6. Plan to share project outcomes 



* Code will be shared via the open-source GitHub repository of [xbitinfo](https://github.com/observingClouds/xbitinfo)
* Blog post
* Collaboration with ECMWF mentors on a journal paper
* A short version of the work can be presented at EGU next year and also submitted to a workshop at an AI conference such as the ClimateChangeAI workshops 

References:

    Klöwer, M. 2021. “Low-Precision Climate Computing: Preserving Information despite Fewer Bits.” http://purl.org/dc/dcmitype/Text, University of Oxford. 

    Klöwer, Milan, Miha Razinger, Juan J. Dominguez, Peter D. Düben, and Tim N. Palmer. 2021. “Compressing Atmospheric Data into Its Real Information Content.” _Nature Computational Science_ 1(11):713–24. doi: 10.1038/s43588-021-00156-2. 
    
    Schulz, Hauke, Aaron Spring, and Milan Klöwer. 2022.“Xbitinfo: Compress Datasets Based on Their Information Content,” October 27. 


## [Not submitted]
### 7. Appendices 

1. **[Thoughts on regionally varying keep bits](https://github.com/observingClouds/xbitinfo/discussions/160) [GitHub discussion]**
   * How should regions be defined? As a list of slices? By creating sub-(data)sets?
   * How should this be saved in a dataset?
   * Are there cases when the compression would benefit from chunk dependent compressors? Should zarr support different compressors per chunk?
   * How can we ensure that Dask workers can calculate the keepbits for each chunk in parallel? 
   * Should the division be static or dynamic? 
   * What criteria should be considered to define a chunk? 
   * Parallel compression of different chunks? 
   * Are “boring” regions the same for all events of interest? Any similarities? 

Research:

| Resource     | Description (❗: important)     | Status     |
|---|---|---|
| (Klöwer 2021)     | ❗Ph.D. thesis: "Low-precision climate computing: preserving information despite fewer bits"  (thank you Klöwer for the quality of this thesis)     |      |
| ❗ Thoughts on regionally varying keep bits      | ❗     |      |
| (Schulz, Spring, and Klöwer 2022)     | Presentation of xbitinfo     |      |
| ELefridge     |      |      |
| (Klöwer et al. 2021)     | ❗Paper: "Compressing atmospheric data into its real information content"     |      |
| Getting Started with xarray      | xarray tutorial     |      |
| xarray-contrib/xarray-tutorial      | xarray tutorial     |      |
| Quickstart with xbitinfo     | xbitinfo tutorial     |      |
| (PDF) NetCDF Compression Improvements      | NetCDF Compression Improvements     |      |
| JPEG compression 	     | Block splitting (8x8) before DCT     |      |
|      |      |      |