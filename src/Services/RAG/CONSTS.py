CHAT_ENDPOINT = ("https://ml-cb4a4d8b-dea.env-hack.svbr-nqvp.int.cldr.work/namespaces/serving-default/endpoints/llama-3"
                 "-1-70b/v1/chat/completions")
EMBEDDING_ENDPOINT = ("https://ml-cb4a4d8b-dea.env-hack.svbr-nqvp.int.cldr.work/namespaces/serving-default/endpoints"
                      "/snowflake-a100/v1/embeddings")
OPENAI_API_KEY = ("eyJraWQiOiJjMDBjNmRlNGE1MjIyYTk1IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ"
                  ".eyJzdWIiOiJjc3NvX3ByYW5lZXRrIiwiYXVkIjoiaHR0cHM6Ly9kZS5zdmJyLW5xdnAuaW50LmNsZHIud29yayIsIm5iZiI6MTcyNjQ4OTExNCwiaXNzIjoiaHR0cHM6Ly9jb25zb2xlYXV0aC50aHVuZGVyaGVhZC1pbnQuY2xvdWRlcmEuY29tL2M4ZGJkZTRiLWNjY2UtNGY4ZC1hNTgxLTgzMDk3MGJhNDkwOCIsImdyb3VwcyI6InRlc3Qtc2F1cmFiaHMtZ3JvdXAtNCB0ZXN0LXNhdXJhYmhzLWdyb3VwLTUgdGVzdC1zYXVyYWJocy1ncm91cC03IHRlc3Qtc2F1cmFiaHMtZ3JvdXAtOCB0ZXN0LXNhdXJhYmhzLWdyb3VwLTIgdGVzdC1zYXVyYWJocy1ncm91cC05IHRlc3Qtc2F1cmFiaHMtZ3JvdXAtNiBlbmctbWwtdGVhbSB0ZXN0LXNhdXJhYmhzLWdyb3VwLTEgdGVzdC1zYXVyYWJocy1ncm91cC0zIHRlc3Qtc2F1cmFiaHMtZ3JvdXAtMTAgX2NfY21fYWRtaW5zXzQ0ZGEyNzczIF9jX21sX3VzZXJzXzMxNWJhNTc4IF9jX2hiYXNlX2FkbWluc18zMTViYTU3OCBfY19lZm1fYWRtaW5zXzZlZTI0ODZiIF9jX2hiYXNlX2FkbWluc182M2MyN2Y5YiBfY19lZm1fYWRtaW5zXzMxNWJhNTc4IF9jX25pZmlfcmVnaXN0cnlfYWRtaW5zXzZlZTI0ODZiIF9jX2tub3hfYWRtaW5zXzEzMmRhODcwIF9jX3plcHBlbGluX2FkbWluc182ZWUyNDg2YiBfY19yYW5nZXJfYWRtaW5zXzQ0ZGEyNzczIF9jX25pZmlfYWRtaW5zXzMxNWJhNTc4IF9jX2hiYXNlX2FkbWluc182ZWUyNDg2YiBfY19uaWZpX3JlZ2lzdHJ5X2FkbWluc18zMTViYTU3OCBfY19yYW5nZXJfYWRtaW5zXzQ0OWU1ZDIwIF9jX2hiYXNlX2FkbWluc18xMzJkYTg3MCBfY19jbV9hZG1pbnNfMTMyZGE4NzAgX2Nfa25veF9hZG1pbnNfNjNjMjdmOWIgX2NfbWxfYWRtaW5zXzEzMmRhODcwIF9jX21sX2FkbWluc18yM2Y2NjYzNyBfY19uaWZpX3JlZ2lzdHJ5X2FkbWluc182M2MyN2Y5YiBfY19tbF91c2Vyc180NDllNWQyMCBfY19tbF91c2Vyc18zNjAxNzU5ZCBfY19lbnZfYXNzaWduZWVzXzZlZTI0ODZiIF9jX2NtX2FkbWluc182M2MyN2Y5YiBfY19lbnZfYXNzaWduZWVzXzMxNWJhNTc4IF9jX2VmbV9hZG1pbnNfNjNjMjdmOWIgX2NfY21fYWRtaW5zXzQ0OWU1ZDIwIF9jX2Vudl9hc3NpZ25lZXNfNDRkYTI3NzMgX2NfbmlmaV9hZG1pbnNfMTMyZGE4NzAgX2NfbWxfYnVzaW5lc3NfdXNlcnNfMTMyZGE4NzAgX2NfY21fYWRtaW5zXzMxNWJhNTc4IF9jX25pZmlfYWRtaW5zXzZlZTI0ODZiIF9jX3plcHBlbGluX2FkbWluc18xMzJkYTg3MCBfY19yYW5nZXJfYWRtaW5zXzEzMmRhODcwIF9jX25pZmlfcmVnaXN0cnlfYWRtaW5zXzQ0OWU1ZDIwIF9jX2VmbV9hZG1pbnNfNDRkYTI3NzMgX2NfcmFuZ2VyX2FkbWluc182ZWUyNDg2YiBfY19lbnZfYXNzaWduZWVzXzEzMmRhODcwIF9jX2Vudl9hc3NpZ25lZXNfNDQ5ZTVkMjAgX2NfY21fYWRtaW5zXzZlZTI0ODZiIF9jX21sX3VzZXJzXzQ0ZGEyNzczIF9jX3plcHBlbGluX2FkbWluc180NGRhMjc3MyBfY19yYW5nZXJfYWRtaW5zXzMxNWJhNTc4IF9jX21sX2J1c2luZXNzX3VzZXJzXzIzZjY2NjM3IF9jX25pZmlfYWRtaW5zXzQ0OWU1ZDIwIF9jX25pZmlfcmVnaXN0cnlfYWRtaW5zXzQ0ZGEyNzczIF9jX2Vudl9hc3NpZ25lZXNfNjNjMjdmOWIgX2NfbmlmaV9yZWdpc3RyeV9hZG1pbnNfMTMyZGE4NzAgX2NfbmlmaV9hZG1pbnNfNDRkYTI3NzMgX2NfemVwcGVsaW5fYWRtaW5zXzQ0OWU1ZDIwIF9jX2tub3hfYWRtaW5zXzMxNWJhNTc4IF9jX21sX3VzZXJzXzEzMmRhODcwIF9jX25pZmlfYWRtaW5zXzYzYzI3ZjliIF9jX2VmbV9hZG1pbnNfNDQ5ZTVkMjAgX2Nfa25veF9hZG1pbnNfNDRkYTI3NzMgX2NfemVwcGVsaW5fYWRtaW5zXzYzYzI3ZjliIF9jX3Jhbmdlcl9hZG1pbnNfNjNjMjdmOWIgX2NfaGJhc2VfYWRtaW5zXzQ0OWU1ZDIwIF9jX21sX3VzZXJzXzIzZjY2NjM3IF9jX21sX2FkbWluc180NGRhMjc3MyBfY19tbF91c2Vyc19jM2QyYzY5IF9jX21sX2FkbWluc180NDllNWQyMCBfY196ZXBwZWxpbl9hZG1pbnNfMzE1YmE1NzggX2Nfa25veF9hZG1pbnNfNmVlMjQ4NmIgX2NfbWxfYWRtaW5zXzMxNWJhNTc4IF9jX2hiYXNlX2FkbWluc180NGRhMjc3MyBfY19rbm94X2FkbWluc180NDllNWQyMCBfY19lZm1fYWRtaW5zXzEzMmRhODcwIF9jX2Vudl9wcml2aWxlZ2VkX3VzZXJzXzEzMmRhODcwIiwiZXhwIjoxNzMyNDg5MTE0LCJ0eXBlIjoidXNlciIsImdpdmVuX25hbWUiOiJQcmFuZWV0IiwiZmFtaWx5X25hbWUiOiJLb25kZXRpIiwiZW1haWwiOiJwcmFuZWV0a0BjbG91ZGVyYS5jb20ifQ.OwDSn3WNLFRgebXBCFKy0BT1tOhNPis6mnuoipjYauI_fTVg2zPVUWG9Eq87EFxHWjxwm8JicadOUOp8ZqKSkwyC-qTUkMCz4jjEQ1ExK_pga-OHu5fTp45VtrVQFBcEoSaMMb95c7Ivg66C1FtT0wHLEAhh3ZngEYpjcXHu5Ccyif7A6Y891RS-_m86eFrBH5-NI1beSuamxSmNp5V6kovFWXAJCYMLqHnZS-0vpGFOokbdj4PsNrmYllzmaAKG9lqWMaRoNMx7aDzut05CVlNGLnJEKNo9b9cxY6jtAm9PPQ68t2eMqC_CU6PnKY-2zrLgSnHaVrJdDpMs0CQZKg")
OPENAI_API_BASE = ("https://ml-cb4a4d8b-dea.env-hack.svbr-nqvp.int.cldr.work/namespaces/serving-default/endpoints"
                   "/llama-3-1-70b/v1")
OPENAI_MODEL_NAME = "6lbx-oajq-2ehb-irio"
