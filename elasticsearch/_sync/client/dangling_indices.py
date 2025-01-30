#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import typing as t

from elastic_transport import ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class DanglingIndicesClient(NamespacedClient):

    @_rewrite_parameters()
    def delete_dangling_index(
        self,
        *,
        index_uuid: str,
        accept_data_loss: bool,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete a dangling index.
          If Elasticsearch encounters index data that is absent from the current cluster state, those indices are considered to be dangling.
          For example, this can happen if you delete more than <code>cluster.indices.tombstones.size</code> indices while an Elasticsearch node is offline.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/dangling-index-delete.html>`_

        :param index_uuid: The UUID of the index to delete. Use the get dangling indices
            API to find the UUID.
        :param accept_data_loss: This parameter must be set to true to acknowledge that
            it will no longer be possible to recove data from the dangling index.
        :param master_timeout: Specify timeout for connection to master
        :param timeout: Explicit operation timeout
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index_uuid'")
        if accept_data_loss is None:
            raise ValueError("Empty value passed for parameter 'accept_data_loss'")
        __path_parts: t.Dict[str, str] = {"index_uuid": _quote(index_uuid)}
        __path = f'/_dangling/{__path_parts["index_uuid"]}'
        __query: t.Dict[str, t.Any] = {}
        if accept_data_loss is not None:
            __query["accept_data_loss"] = accept_data_loss
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="dangling_indices.delete_dangling_index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def import_dangling_index(
        self,
        *,
        index_uuid: str,
        accept_data_loss: bool,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Import a dangling index.</p>
          <p>If Elasticsearch encounters index data that is absent from the current cluster state, those indices are considered to be dangling.
          For example, this can happen if you delete more than <code>cluster.indices.tombstones.size</code> indices while an Elasticsearch node is offline.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/dangling-index-import.html>`_

        :param index_uuid: The UUID of the index to import. Use the get dangling indices
            API to locate the UUID.
        :param accept_data_loss: This parameter must be set to true to import a dangling
            index. Because Elasticsearch cannot know where the dangling index data came
            from or determine which shard copies are fresh and which are stale, it cannot
            guarantee that the imported data represents the latest state of the index
            when it was last in the cluster.
        :param master_timeout: Specify timeout for connection to master
        :param timeout: Explicit operation timeout
        """
        if index_uuid in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index_uuid'")
        if accept_data_loss is None:
            raise ValueError("Empty value passed for parameter 'accept_data_loss'")
        __path_parts: t.Dict[str, str] = {"index_uuid": _quote(index_uuid)}
        __path = f'/_dangling/{__path_parts["index_uuid"]}'
        __query: t.Dict[str, t.Any] = {}
        if accept_data_loss is not None:
            __query["accept_data_loss"] = accept_data_loss
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="dangling_indices.import_dangling_index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def list_dangling_indices(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get the dangling indices.</p>
          <p>If Elasticsearch encounters index data that is absent from the current cluster state, those indices are considered to be dangling.
          For example, this can happen if you delete more than <code>cluster.indices.tombstones.size</code> indices while an Elasticsearch node is offline.</p>
          <p>Use this API to list dangling indices, which you can then import or delete.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/dangling-indices-list.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_dangling"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="dangling_indices.list_dangling_indices",
            path_parts=__path_parts,
        )
