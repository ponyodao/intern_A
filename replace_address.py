def replace_address(address):
  if "丁目" in address:
    address1 = address.replace("丁目","-")
    if "番地" in address:
      address2 = address1.replace("番地","-")
    elif "番" in address:
      address2 = address1.replace("番","-")
    else:
      address2 = address1
  else:
    if "番地" in address:
      address2 = address.replace("番地","-")
    elif "番" in address:
      address2 = address.replace("番","-")
    else:
      address2 = address

  return address2