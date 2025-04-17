# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.connector.v1 import task_add_params, task_list_params
from .....types.api.connector.v1.task_add_response import TaskAddResponse
from .....types.api.connector.v1.task_list_response import TaskListResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: task_list_params.Limitation,
        closed_utc: Optional[task_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[task_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        deadline_utc: Optional[task_list_params.DeadlineUtc] | NotGiven = NOT_GIVEN,
        department_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        task_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Returns all tasks of the enterprise, filtered by identifiers or other filters.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          closed_utc: Interval in which the Task was closed.

          created_utc: Interval in which the Task was created.

          deadline_utc: Interval in which the Task has a deadline.

          department_ids: Unique identifiers of
              [Departments](https://mews-systems.gitbook.io/connector-api/operations/departments/#department).
              Not possible to be used standalone, needs to be used in combination with other
              filters.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_order_ids: Unique identifiers of service orders (reservations or product service orders).

          task_ids: Unique identifiers of
              [Tasks](https://mews-systems.gitbook.io/connector-api/operations/#task).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/tasks/getAll",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "closed_utc": closed_utc,
                    "created_utc": created_utc,
                    "deadline_utc": deadline_utc,
                    "department_ids": department_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_order_ids": service_order_ids,
                    "task_ids": task_ids,
                },
                task_list_params.TaskListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskListResponse,
        )

    def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        deadline_utc: Union[str, datetime],
        name: str,
        department_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        service_order_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskAddResponse:
        """
        Adds a new task to the enterprise, optionally to a specified department.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          deadline_utc: Deadline of the task in UTC timezone in ISO 8601 format.

          name: Name (or title) of the task.

          department_id: Unique identifier of the
              [Department](https://mews-systems.gitbook.io/connector-api/operations/departments/#department)
              the task is addressed to.

          description: Further decription of the task.

          service_order_id: Unique identifier of the service order (reservation or product service order)
              the task is linked with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/connector/v1/tasks/add",
            body=maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "deadline_utc": deadline_utc,
                    "name": name,
                    "department_id": department_id,
                    "description": description,
                    "service_order_id": service_order_id,
                },
                task_add_params.TaskAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAddResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/eivl/pymews#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/eivl/pymews#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        limitation: task_list_params.Limitation,
        closed_utc: Optional[task_list_params.ClosedUtc] | NotGiven = NOT_GIVEN,
        created_utc: Optional[task_list_params.CreatedUtc] | NotGiven = NOT_GIVEN,
        deadline_utc: Optional[task_list_params.DeadlineUtc] | NotGiven = NOT_GIVEN,
        department_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enterprise_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        service_order_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        task_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Returns all tasks of the enterprise, filtered by identifiers or other filters.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          limitation: Limitation on the quantity of data returned.

          closed_utc: Interval in which the Task was closed.

          created_utc: Interval in which the Task was created.

          deadline_utc: Interval in which the Task has a deadline.

          department_ids: Unique identifiers of
              [Departments](https://mews-systems.gitbook.io/connector-api/operations/departments/#department).
              Not possible to be used standalone, needs to be used in combination with other
              filters.

          enterprise_ids: Unique identifiers of the Enterprises. If not specified, the operation returns
              data for all enterprises within scope of the Access Token.

          service_order_ids: Unique identifiers of service orders (reservations or product service orders).

          task_ids: Unique identifiers of
              [Tasks](https://mews-systems.gitbook.io/connector-api/operations/#task).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/tasks/getAll",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "limitation": limitation,
                    "closed_utc": closed_utc,
                    "created_utc": created_utc,
                    "deadline_utc": deadline_utc,
                    "department_ids": department_ids,
                    "enterprise_ids": enterprise_ids,
                    "service_order_ids": service_order_ids,
                    "task_ids": task_ids,
                },
                task_list_params.TaskListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskListResponse,
        )

    async def add(
        self,
        *,
        access_token: str,
        client: str,
        client_token: str,
        deadline_utc: Union[str, datetime],
        name: str,
        department_id: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        service_order_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskAddResponse:
        """
        Adds a new task to the enterprise, optionally to a specified department.

        Args:
          access_token: Access token of the client application.

          client: Name and version of the client application.

          client_token: Token identifying the client application.

          deadline_utc: Deadline of the task in UTC timezone in ISO 8601 format.

          name: Name (or title) of the task.

          department_id: Unique identifier of the
              [Department](https://mews-systems.gitbook.io/connector-api/operations/departments/#department)
              the task is addressed to.

          description: Further decription of the task.

          service_order_id: Unique identifier of the service order (reservation or product service order)
              the task is linked with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/connector/v1/tasks/add",
            body=await async_maybe_transform(
                {
                    "access_token": access_token,
                    "client": client,
                    "client_token": client_token,
                    "deadline_utc": deadline_utc,
                    "name": name,
                    "department_id": department_id,
                    "description": description,
                    "service_order_id": service_order_id,
                },
                task_add_params.TaskAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskAddResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.add = to_raw_response_wrapper(
            tasks.add,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.add = async_to_raw_response_wrapper(
            tasks.add,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.add = to_streamed_response_wrapper(
            tasks.add,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.add = async_to_streamed_response_wrapper(
            tasks.add,
        )
