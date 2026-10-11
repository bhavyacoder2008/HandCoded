from shop import get_balance,get_item_price,buy_item

print(get_balance())
print(get_item_price("banana"))

print(buy_item("apple", 10))

tools = [{"name": "get_balance", "args": {}}, {"name": "get_item_price", "args": ["item"]}, {"name": "buy_item", "args": ["item", "quantity"]}]
tool_names = [i["name"] for i in tools]

function_mapping = {
    "get_balance": get_balance,
    "get_item_price": get_item_price,
    "buy_item": buy_item
}

def execute_tool(tool_name: str, arguments: dict) -> dict:
    if tool_name not in tool_names:
        return {"success": False, "data": None, "error": "Tool not found"}
    
    tool_info = {}
    for i in tools:
        if tool_name == i["name"]:
            tool_info = i
            break
    
    tools_argument = tool_info["args"] # it is a list having names of the arguments accepted by that specific tool
    matching_list_from_function_argument = list(arguments)
    if tools_argument != matching_list_from_function_argument:
        return {"success": False, "data": None, "error": "Invalid tool"}
    
    selected_function = function_mapping[tool_name]
    return selected_function()
    

print(execute_tool("get_item_price", {"item": "apple"}))