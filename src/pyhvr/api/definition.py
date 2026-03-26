"""Definition interface."""

from __future__ import annotations

from typing import Any


class DefinitionMixin:
    def get_definition(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition")

    def get_definition_change_events(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/change_events")

    def list_channels(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels")

    def get_channel(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}")

    def get_channel_actions(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/actions")

    def list_channel_loc_groups(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups")

    def get_channel_loc_group(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}")

    def get_channel_loc_group_members(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members")

    def list_channel_tables(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables")

    def get_channel_table(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}")

    def get_table_cols(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols")

    def get_hub_actions(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/hub_actions")

    def list_locs(self, hub: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/locs")

    def get_loc(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/locs/{loc}")

    def get_loc_actions(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/locs/{loc}/actions")

    def get_loc_props(self, hub: str, loc: str) -> dict[str, Any]:
        return self._request("GET", f"/hubs/{hub}/definition/locs/{loc}/props")

    def modify_action(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/action_modify", json=body)

    def replace_action(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/action_replace", json=body)

    def create_channel(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels", json=body)

    def delete_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/actions_delete", json=body)

    def create_channel_loc_group(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups", json=body)

    def delete_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members_delete", json=body)

    def rename_channel_loc_group(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/rename", json=body)

    def rename_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/rename", json=body)

    def add_channel_table(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    def delete_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols_delete", json=body)

    def rename_table(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/rename", json=body)

    def delete_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables_delete", json=body)

    def delete_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/hub_actions_delete", json=body)

    def import_definition(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/import", json=body)

    def analyze_import(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/import_analyze", json=body)

    def create_loc(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/locs", json=body)

    def delete_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/actions_delete", json=body)

    def copy_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/copy", json=body)

    def delete_loc_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/props_delete", json=body)

    def rename_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/rename", json=body)

    def patch_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}", json=body)

    def patch_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/actions", json=body)

    def patch_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members", json=body)

    def patch_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    def patch_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols", json=body)

    def patch_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/hub_actions", json=body)

    def patch_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/locs/{loc}/actions", json=body)

    def patch_loc_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PATCH", f"/hubs/{hub}/definition/locs/{loc}/props", json=body)

    def put_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}", json=body)

    def put_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/actions", json=body)

    def put_channel_loc_group(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}", json=body)

    def put_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members", json=body)

    def put_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    def put_channel_table(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}", json=body)

    def put_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols", json=body)

    def put_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/hub_actions", json=body)

    def put_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/locs/{loc}", json=body)

    def put_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return self._request("PUT", f"/hubs/{hub}/definition/locs/{loc}/actions", json=body)

    def delete_channel(self, hub: str, channel: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}")

    def delete_channel_loc_group(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}")

    def delete_channel_loc_group_member(self, hub: str, channel: str, group: str, member: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members/{member}")

    def delete_channel_table(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}")


class AsyncDefinitionMixin:
    async def get_definition(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition")

    async def get_definition_change_events(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/change_events")

    async def list_channels(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels")

    async def get_channel(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}")

    async def get_channel_actions(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/actions")

    async def list_channel_loc_groups(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups")

    async def get_channel_loc_group(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}")

    async def get_channel_loc_group_members(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members")

    async def list_channel_tables(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables")

    async def get_channel_table(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}")

    async def get_table_cols(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols")

    async def get_hub_actions(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/hub_actions")

    async def list_locs(self, hub: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/locs")

    async def get_loc(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/locs/{loc}")

    async def get_loc_actions(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/locs/{loc}/actions")

    async def get_loc_props(self, hub: str, loc: str) -> dict[str, Any]:
        return await self._request("GET", f"/hubs/{hub}/definition/locs/{loc}/props")

    async def modify_action(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/action_modify", json=body)

    async def replace_action(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/action_replace", json=body)

    async def create_channel(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels", json=body)

    async def delete_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/actions_delete", json=body)

    async def create_channel_loc_group(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups", json=body)

    async def delete_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members_delete", json=body)

    async def rename_channel_loc_group(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/rename", json=body)

    async def rename_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/rename", json=body)

    async def add_channel_table(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    async def delete_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols_delete", json=body)

    async def rename_table(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/rename", json=body)

    async def delete_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/channels/{channel}/tables_delete", json=body)

    async def delete_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/hub_actions_delete", json=body)

    async def import_definition(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/import", json=body)

    async def analyze_import(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/import_analyze", json=body)

    async def create_loc(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/locs", json=body)

    async def delete_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/actions_delete", json=body)

    async def copy_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/copy", json=body)

    async def delete_loc_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/props_delete", json=body)

    async def rename_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("POST", f"/hubs/{hub}/definition/locs/{loc}/rename", json=body)

    async def patch_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}", json=body)

    async def patch_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/actions", json=body)

    async def patch_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members", json=body)

    async def patch_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    async def patch_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols", json=body)

    async def patch_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/hub_actions", json=body)

    async def patch_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/locs/{loc}/actions", json=body)

    async def patch_loc_props(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PATCH", f"/hubs/{hub}/definition/locs/{loc}/props", json=body)

    async def put_channel(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}", json=body)

    async def put_channel_actions(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/actions", json=body)

    async def put_channel_loc_group(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}", json=body)

    async def put_channel_loc_group_members(self, hub: str, channel: str, group: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members", json=body)

    async def put_channel_tables(self, hub: str, channel: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables", json=body)

    async def put_channel_table(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}", json=body)

    async def put_table_cols(self, hub: str, channel: str, table: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}/cols", json=body)

    async def put_hub_actions(self, hub: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/hub_actions", json=body)

    async def put_loc(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/locs/{loc}", json=body)

    async def put_loc_actions(self, hub: str, loc: str, body: dict | None = None) -> dict[str, Any]:
        return await self._request("PUT", f"/hubs/{hub}/definition/locs/{loc}/actions", json=body)

    async def delete_channel(self, hub: str, channel: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}")

    async def delete_channel_loc_group(self, hub: str, channel: str, group: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}")

    async def delete_channel_loc_group_member(self, hub: str, channel: str, group: str, member: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/loc_groups/{group}/members/{member}")

    async def delete_channel_table(self, hub: str, channel: str, table: str) -> dict[str, Any]:
        return await self._request("DELETE", f"/hubs/{hub}/definition/channels/{channel}/tables/{table}")
