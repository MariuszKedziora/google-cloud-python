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
# Generated code. DO NOT EDIT!
#
# Snippet for InsertLocalInventory
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-merchant-inventories


# [START merchantapi_v1beta_generated_LocalInventoryService_InsertLocalInventory_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import merchant_inventories_v1beta


async def sample_insert_local_inventory():
    # Create a client
    client = merchant_inventories_v1beta.LocalInventoryServiceAsyncClient()

    # Initialize request argument(s)
    local_inventory = merchant_inventories_v1beta.LocalInventory()
    local_inventory.store_code = "store_code_value"

    request = merchant_inventories_v1beta.InsertLocalInventoryRequest(
        parent="parent_value",
        local_inventory=local_inventory,
    )

    # Make the request
    response = await client.insert_local_inventory(request=request)

    # Handle the response
    print(response)

# [END merchantapi_v1beta_generated_LocalInventoryService_InsertLocalInventory_async]
