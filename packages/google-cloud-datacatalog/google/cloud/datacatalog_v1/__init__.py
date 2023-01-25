# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.datacatalog_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.data_catalog import DataCatalogAsyncClient, DataCatalogClient
from .services.policy_tag_manager import (
    PolicyTagManagerAsyncClient,
    PolicyTagManagerClient,
)
from .services.policy_tag_manager_serialization import (
    PolicyTagManagerSerializationAsyncClient,
    PolicyTagManagerSerializationClient,
)
from .types.bigquery import (
    BigQueryConnectionSpec,
    BigQueryRoutineSpec,
    CloudSqlBigQueryConnectionSpec,
)
from .types.common import IntegratedSystem, PersonalDetails
from .types.data_source import DataSource, StorageProperties
from .types.datacatalog import (
    BusinessContext,
    Contacts,
    CreateEntryGroupRequest,
    CreateEntryRequest,
    CreateTagRequest,
    CreateTagTemplateFieldRequest,
    CreateTagTemplateRequest,
    DatabaseTableSpec,
    DataSourceConnectionSpec,
    DeleteEntryGroupRequest,
    DeleteEntryRequest,
    DeleteTagRequest,
    DeleteTagTemplateFieldRequest,
    DeleteTagTemplateRequest,
    Entry,
    EntryGroup,
    EntryOverview,
    EntryType,
    FilesetSpec,
    GetEntryGroupRequest,
    GetEntryRequest,
    GetTagTemplateRequest,
    ListEntriesRequest,
    ListEntriesResponse,
    ListEntryGroupsRequest,
    ListEntryGroupsResponse,
    ListTagsRequest,
    ListTagsResponse,
    LookupEntryRequest,
    ModifyEntryContactsRequest,
    ModifyEntryOverviewRequest,
    RenameTagTemplateFieldEnumValueRequest,
    RenameTagTemplateFieldRequest,
    RoutineSpec,
    SearchCatalogRequest,
    SearchCatalogResponse,
    StarEntryRequest,
    StarEntryResponse,
    UnstarEntryRequest,
    UnstarEntryResponse,
    UpdateEntryGroupRequest,
    UpdateEntryRequest,
    UpdateTagRequest,
    UpdateTagTemplateFieldRequest,
    UpdateTagTemplateRequest,
)
from .types.dataplex_spec import (
    DataplexExternalTable,
    DataplexFilesetSpec,
    DataplexSpec,
    DataplexTableSpec,
)
from .types.gcs_fileset_spec import GcsFilesetSpec, GcsFileSpec
from .types.physical_schema import PhysicalSchema
from .types.policytagmanager import (
    CreatePolicyTagRequest,
    CreateTaxonomyRequest,
    DeletePolicyTagRequest,
    DeleteTaxonomyRequest,
    GetPolicyTagRequest,
    GetTaxonomyRequest,
    ListPolicyTagsRequest,
    ListPolicyTagsResponse,
    ListTaxonomiesRequest,
    ListTaxonomiesResponse,
    PolicyTag,
    Taxonomy,
    UpdatePolicyTagRequest,
    UpdateTaxonomyRequest,
)
from .types.policytagmanagerserialization import (
    CrossRegionalSource,
    ExportTaxonomiesRequest,
    ExportTaxonomiesResponse,
    ImportTaxonomiesRequest,
    ImportTaxonomiesResponse,
    InlineSource,
    ReplaceTaxonomyRequest,
    SerializedPolicyTag,
    SerializedTaxonomy,
)
from .types.schema import ColumnSchema, Schema
from .types.search import SearchCatalogResult, SearchResultType
from .types.table_spec import (
    BigQueryDateShardedSpec,
    BigQueryTableSpec,
    TableSourceType,
    TableSpec,
    ViewSpec,
)
from .types.tags import FieldType, Tag, TagField, TagTemplate, TagTemplateField
from .types.timestamps import SystemTimestamps
from .types.usage import UsageSignal, UsageStats

__all__ = (
    "DataCatalogAsyncClient",
    "PolicyTagManagerAsyncClient",
    "PolicyTagManagerSerializationAsyncClient",
    "BigQueryConnectionSpec",
    "BigQueryDateShardedSpec",
    "BigQueryRoutineSpec",
    "BigQueryTableSpec",
    "BusinessContext",
    "CloudSqlBigQueryConnectionSpec",
    "ColumnSchema",
    "Contacts",
    "CreateEntryGroupRequest",
    "CreateEntryRequest",
    "CreatePolicyTagRequest",
    "CreateTagRequest",
    "CreateTagTemplateFieldRequest",
    "CreateTagTemplateRequest",
    "CreateTaxonomyRequest",
    "CrossRegionalSource",
    "DataCatalogClient",
    "DataSource",
    "DataSourceConnectionSpec",
    "DatabaseTableSpec",
    "DataplexExternalTable",
    "DataplexFilesetSpec",
    "DataplexSpec",
    "DataplexTableSpec",
    "DeleteEntryGroupRequest",
    "DeleteEntryRequest",
    "DeletePolicyTagRequest",
    "DeleteTagRequest",
    "DeleteTagTemplateFieldRequest",
    "DeleteTagTemplateRequest",
    "DeleteTaxonomyRequest",
    "Entry",
    "EntryGroup",
    "EntryOverview",
    "EntryType",
    "ExportTaxonomiesRequest",
    "ExportTaxonomiesResponse",
    "FieldType",
    "FilesetSpec",
    "GcsFileSpec",
    "GcsFilesetSpec",
    "GetEntryGroupRequest",
    "GetEntryRequest",
    "GetPolicyTagRequest",
    "GetTagTemplateRequest",
    "GetTaxonomyRequest",
    "ImportTaxonomiesRequest",
    "ImportTaxonomiesResponse",
    "InlineSource",
    "IntegratedSystem",
    "ListEntriesRequest",
    "ListEntriesResponse",
    "ListEntryGroupsRequest",
    "ListEntryGroupsResponse",
    "ListPolicyTagsRequest",
    "ListPolicyTagsResponse",
    "ListTagsRequest",
    "ListTagsResponse",
    "ListTaxonomiesRequest",
    "ListTaxonomiesResponse",
    "LookupEntryRequest",
    "ModifyEntryContactsRequest",
    "ModifyEntryOverviewRequest",
    "PersonalDetails",
    "PhysicalSchema",
    "PolicyTag",
    "PolicyTagManagerClient",
    "PolicyTagManagerSerializationClient",
    "RenameTagTemplateFieldEnumValueRequest",
    "RenameTagTemplateFieldRequest",
    "ReplaceTaxonomyRequest",
    "RoutineSpec",
    "Schema",
    "SearchCatalogRequest",
    "SearchCatalogResponse",
    "SearchCatalogResult",
    "SearchResultType",
    "SerializedPolicyTag",
    "SerializedTaxonomy",
    "StarEntryRequest",
    "StarEntryResponse",
    "StorageProperties",
    "SystemTimestamps",
    "TableSourceType",
    "TableSpec",
    "Tag",
    "TagField",
    "TagTemplate",
    "TagTemplateField",
    "Taxonomy",
    "UnstarEntryRequest",
    "UnstarEntryResponse",
    "UpdateEntryGroupRequest",
    "UpdateEntryRequest",
    "UpdatePolicyTagRequest",
    "UpdateTagRequest",
    "UpdateTagTemplateFieldRequest",
    "UpdateTagTemplateRequest",
    "UpdateTaxonomyRequest",
    "UsageSignal",
    "UsageStats",
    "ViewSpec",
)
