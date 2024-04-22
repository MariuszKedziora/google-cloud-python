# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.maps.mapsplatformdatasets_v1alpha import gapic_version as package_version

__version__ = package_version.__version__


from .services.maps_platform_datasets_v1_alpha import MapsPlatformDatasetsV1AlphaClient
from .services.maps_platform_datasets_v1_alpha import MapsPlatformDatasetsV1AlphaAsyncClient

from .types.data_source import GcsSource
from .types.data_source import LocalFileSource
from .types.data_source import FileFormat
from .types.dataset import Dataset
from .types.dataset import State
from .types.dataset import Usage
from .types.maps_platform_datasets import CreateDatasetRequest
from .types.maps_platform_datasets import DeleteDatasetRequest
from .types.maps_platform_datasets import DeleteDatasetVersionRequest
from .types.maps_platform_datasets import GetDatasetRequest
from .types.maps_platform_datasets import ListDatasetsRequest
from .types.maps_platform_datasets import ListDatasetsResponse
from .types.maps_platform_datasets import ListDatasetVersionsRequest
from .types.maps_platform_datasets import ListDatasetVersionsResponse
from .types.maps_platform_datasets import UpdateDatasetMetadataRequest

__all__ = (
    'MapsPlatformDatasetsV1AlphaAsyncClient',
'CreateDatasetRequest',
'Dataset',
'DeleteDatasetRequest',
'DeleteDatasetVersionRequest',
'FileFormat',
'GcsSource',
'GetDatasetRequest',
'ListDatasetVersionsRequest',
'ListDatasetVersionsResponse',
'ListDatasetsRequest',
'ListDatasetsResponse',
'LocalFileSource',
'MapsPlatformDatasetsV1AlphaClient',
'State',
'UpdateDatasetMetadataRequest',
'Usage',
)
