# The order status would be:
# order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

def choiceAction(inAction):
    if (int(inAction) == 1):
        return "Print Order Dictionary"
    elif inAction == 2:
        return "Add Order"
    elif inAction == 3:
        return "Update Existing Order Status"
    elif inAction == 4:
        return "STRETCH-update Order"
    elif inAction == 5:
        return "Delete Order"