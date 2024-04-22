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
from google.shopping.css import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.css_v1.services.account_labels_service.client import AccountLabelsServiceClient
from google.shopping.css_v1.services.account_labels_service.async_client import AccountLabelsServiceAsyncClient
from google.shopping.css_v1.services.accounts_service.client import AccountsServiceClient
from google.shopping.css_v1.services.accounts_service.async_client import AccountsServiceAsyncClient
from google.shopping.css_v1.services.css_product_inputs_service.client import CssProductInputsServiceClient
from google.shopping.css_v1.services.css_product_inputs_service.async_client import CssProductInputsServiceAsyncClient
from google.shopping.css_v1.services.css_products_service.client import CssProductsServiceClient
from google.shopping.css_v1.services.css_products_service.async_client import CssProductsServiceAsyncClient

from google.shopping.css_v1.types.accounts import Account
from google.shopping.css_v1.types.accounts import GetAccountRequest
from google.shopping.css_v1.types.accounts import ListChildAccountsRequest
from google.shopping.css_v1.types.accounts import ListChildAccountsResponse
from google.shopping.css_v1.types.accounts import UpdateAccountLabelsRequest
from google.shopping.css_v1.types.accounts_labels import AccountLabel
from google.shopping.css_v1.types.accounts_labels import CreateAccountLabelRequest
from google.shopping.css_v1.types.accounts_labels import DeleteAccountLabelRequest
from google.shopping.css_v1.types.accounts_labels import ListAccountLabelsRequest
from google.shopping.css_v1.types.accounts_labels import ListAccountLabelsResponse
from google.shopping.css_v1.types.accounts_labels import UpdateAccountLabelRequest
from google.shopping.css_v1.types.css_product_common import Attributes
from google.shopping.css_v1.types.css_product_common import Certification
from google.shopping.css_v1.types.css_product_common import CssProductStatus
from google.shopping.css_v1.types.css_product_common import ProductDetail
from google.shopping.css_v1.types.css_product_common import ProductDimension
from google.shopping.css_v1.types.css_product_common import ProductWeight
from google.shopping.css_v1.types.css_product_inputs import CssProductInput
from google.shopping.css_v1.types.css_product_inputs import DeleteCssProductInputRequest
from google.shopping.css_v1.types.css_product_inputs import InsertCssProductInputRequest
from google.shopping.css_v1.types.css_products import CssProduct
from google.shopping.css_v1.types.css_products import GetCssProductRequest
from google.shopping.css_v1.types.css_products import ListCssProductsRequest
from google.shopping.css_v1.types.css_products import ListCssProductsResponse

__all__ = ('AccountLabelsServiceClient',
    'AccountLabelsServiceAsyncClient',
    'AccountsServiceClient',
    'AccountsServiceAsyncClient',
    'CssProductInputsServiceClient',
    'CssProductInputsServiceAsyncClient',
    'CssProductsServiceClient',
    'CssProductsServiceAsyncClient',
    'Account',
    'GetAccountRequest',
    'ListChildAccountsRequest',
    'ListChildAccountsResponse',
    'UpdateAccountLabelsRequest',
    'AccountLabel',
    'CreateAccountLabelRequest',
    'DeleteAccountLabelRequest',
    'ListAccountLabelsRequest',
    'ListAccountLabelsResponse',
    'UpdateAccountLabelRequest',
    'Attributes',
    'Certification',
    'CssProductStatus',
    'ProductDetail',
    'ProductDimension',
    'ProductWeight',
    'CssProductInput',
    'DeleteCssProductInputRequest',
    'InsertCssProductInputRequest',
    'CssProduct',
    'GetCssProductRequest',
    'ListCssProductsRequest',
    'ListCssProductsResponse',
)
