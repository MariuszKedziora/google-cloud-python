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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.batch_v1alpha.types import batch, job, resource_allowance, task


class ListJobsPager:
    """A pager for iterating through ``list_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., batch.ListJobsResponse],
        request: batch.ListJobsRequest,
        response: batch.ListJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListJobsRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[batch.ListJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[job.Job]:
        for page in self.pages:
            yield from page.jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobsAsyncPager:
    """A pager for iterating through ``list_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[batch.ListJobsResponse]],
        request: batch.ListJobsRequest,
        response: batch.ListJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListJobsRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[batch.ListJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[job.Job]:
        async def async_generator():
            async for page in self.pages:
                for response in page.jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTasksPager:
    """A pager for iterating through ``list_tasks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListTasksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tasks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTasks`` requests and continue to iterate
    through the ``tasks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListTasksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., batch.ListTasksResponse],
        request: batch.ListTasksRequest,
        response: batch.ListTasksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListTasksRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListTasksResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListTasksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[batch.ListTasksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[task.Task]:
        for page in self.pages:
            yield from page.tasks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTasksAsyncPager:
    """A pager for iterating through ``list_tasks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListTasksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tasks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTasks`` requests and continue to iterate
    through the ``tasks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListTasksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[batch.ListTasksResponse]],
        request: batch.ListTasksRequest,
        response: batch.ListTasksResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListTasksRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListTasksResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListTasksRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[batch.ListTasksResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[task.Task]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tasks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceAllowancesPager:
    """A pager for iterating through ``list_resource_allowances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_allowances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListResourceAllowances`` requests and continue to iterate
    through the ``resource_allowances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., batch.ListResourceAllowancesResponse],
        request: batch.ListResourceAllowancesRequest,
        response: batch.ListResourceAllowancesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListResourceAllowancesRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListResourceAllowancesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[batch.ListResourceAllowancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resource_allowance.ResourceAllowance]:
        for page in self.pages:
            yield from page.resource_allowances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceAllowancesAsyncPager:
    """A pager for iterating through ``list_resource_allowances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_allowances`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListResourceAllowances`` requests and continue to iterate
    through the ``resource_allowances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[batch.ListResourceAllowancesResponse]],
        request: batch.ListResourceAllowancesRequest,
        response: batch.ListResourceAllowancesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.batch_v1alpha.types.ListResourceAllowancesRequest):
                The initial request object.
            response (google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = batch.ListResourceAllowancesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[batch.ListResourceAllowancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[resource_allowance.ResourceAllowance]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_allowances:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
