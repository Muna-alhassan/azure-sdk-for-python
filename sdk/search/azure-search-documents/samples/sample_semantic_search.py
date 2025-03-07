# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_semantic_search.py
DESCRIPTION:
    This sample demonstrates how to use semantic search.
USAGE:
    python sample_semantic_search.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_SEARCH_SERVICE_ENDPOINT - the endpoint of your Azure Cognitive Search service
    2) AZURE_SEARCH_INDEX_NAME - the name of your search index (e.g. "hotels-sample-index")
    3) AZURE_SEARCH_API_KEY - your search API key
"""

import os

def speller():
    # [START speller]
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient

    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")

    credential = AzureKeyCredential(api_key)
    client = SearchClient(endpoint=endpoint,
                          index_name=index_name,
                          credential=credential)
    results = list(client.search(search_text="luxury", query_language="en-us", query_speller="lexicon"))

    for result in results:
        print("{}\n{}\n)".format(result["HotelId"], result["HotelName"]))
    # [END speller]

def semantic_ranking():
    # [START semantic_ranking]
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient

    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")

    credential = AzureKeyCredential(api_key)
    client = SearchClient(endpoint=endpoint,
                          index_name=index_name,
                          credential=credential)
    results = list(client.search(search_text="luxury", query_type="semantic", query_language="en-us"))

    for result in results:
        print("{}\n{}\n)".format(result["HotelId"], result["HotelName"]))
    # [END semantic_ranking]

if __name__ == '__main__':
    speller()
    semantic_ranking()
