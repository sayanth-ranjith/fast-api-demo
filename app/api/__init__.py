from importlib import import_module
from pkgutil import iter_modules

from fastapi import APIRouter


def collect_routers(package_name: str) -> list[APIRouter]:
    package = import_module(package_name)
    routers: list[APIRouter] = []

    for module_info in sorted(iter_modules(package.__path__, package.__name__ + "."), key=lambda item: item.name):
        module = import_module(module_info.name)
        router = getattr(module, "router", None)
        if isinstance(router, APIRouter):
            routers.append(router)
        if module_info.ispkg:
            routers.extend(collect_routers(module_info.name))

    return routers
