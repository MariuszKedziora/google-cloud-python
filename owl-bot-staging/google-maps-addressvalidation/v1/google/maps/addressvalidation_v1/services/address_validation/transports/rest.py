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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


from google.maps.addressvalidation_v1.types import address_validation_service

from .base import AddressValidationTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class AddressValidationRestInterceptor:
    """Interceptor for AddressValidation.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AddressValidationRestTransport.

    .. code-block:: python
        class MyCustomAddressValidationInterceptor(AddressValidationRestInterceptor):
            def pre_provide_validation_feedback(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_provide_validation_feedback(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_address(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_address(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AddressValidationRestTransport(interceptor=MyCustomAddressValidationInterceptor())
        client = AddressValidationClient(transport=transport)


    """
    def pre_provide_validation_feedback(self, request: address_validation_service.ProvideValidationFeedbackRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[address_validation_service.ProvideValidationFeedbackRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for provide_validation_feedback

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AddressValidation server.
        """
        return request, metadata

    def post_provide_validation_feedback(self, response: address_validation_service.ProvideValidationFeedbackResponse) -> address_validation_service.ProvideValidationFeedbackResponse:
        """Post-rpc interceptor for provide_validation_feedback

        Override in a subclass to manipulate the response
        after it is returned by the AddressValidation server but before
        it is returned to user code.
        """
        return response
    def pre_validate_address(self, request: address_validation_service.ValidateAddressRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[address_validation_service.ValidateAddressRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for validate_address

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AddressValidation server.
        """
        return request, metadata

    def post_validate_address(self, response: address_validation_service.ValidateAddressResponse) -> address_validation_service.ValidateAddressResponse:
        """Post-rpc interceptor for validate_address

        Override in a subclass to manipulate the response
        after it is returned by the AddressValidation server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AddressValidationRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AddressValidationRestInterceptor


class AddressValidationRestTransport(AddressValidationTransport):
    """REST backend transport for AddressValidation.

    The service for validating addresses.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'addressvalidation.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[AddressValidationRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'addressvalidation.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or AddressValidationRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ProvideValidationFeedback(AddressValidationRestStub):
        def __hash__(self):
            return hash("ProvideValidationFeedback")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: address_validation_service.ProvideValidationFeedbackRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> address_validation_service.ProvideValidationFeedbackResponse:
            r"""Call the provide validation
        feedback method over HTTP.

            Args:
                request (~.address_validation_service.ProvideValidationFeedbackRequest):
                    The request object. The request for sending validation
                feedback.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.address_validation_service.ProvideValidationFeedbackResponse:
                    The response for validation feedback.

                The response is empty if the feedback is
                sent successfully.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1:provideValidationFeedback',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_provide_validation_feedback(request, metadata)
            pb_request = address_validation_service.ProvideValidationFeedbackRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = address_validation_service.ProvideValidationFeedbackResponse()
            pb_resp = address_validation_service.ProvideValidationFeedbackResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_provide_validation_feedback(resp)
            return resp

    class _ValidateAddress(AddressValidationRestStub):
        def __hash__(self):
            return hash("ValidateAddress")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: address_validation_service.ValidateAddressRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> address_validation_service.ValidateAddressResponse:
            r"""Call the validate address method over HTTP.

            Args:
                request (~.address_validation_service.ValidateAddressRequest):
                    The request object. The request for validating an
                address.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.address_validation_service.ValidateAddressResponse:
                    The response to an address validation
                request.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1:validateAddress',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_validate_address(request, metadata)
            pb_request = address_validation_service.ValidateAddressRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = address_validation_service.ValidateAddressResponse()
            pb_resp = address_validation_service.ValidateAddressResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_validate_address(resp)
            return resp

    @property
    def provide_validation_feedback(self) -> Callable[
            [address_validation_service.ProvideValidationFeedbackRequest],
            address_validation_service.ProvideValidationFeedbackResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProvideValidationFeedback(self._session, self._host, self._interceptor) # type: ignore

    @property
    def validate_address(self) -> Callable[
            [address_validation_service.ValidateAddressRequest],
            address_validation_service.ValidateAddressResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateAddress(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'AddressValidationRestTransport',
)
