# (generated with --quick)

import jauth.serializers
from typing import Any, Type

AuthResultSerializer: Type[jauth.serializers.AuthResultSerializer]
TestCase: Any
User: Any

class Tests(Any):
    user: Any
    def add_test_user(self, email: str = ..., password: str = ...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_serializers(self) -> None: ...
