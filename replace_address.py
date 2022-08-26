import jaconv
def replace_address(address):
  address = address.replace("一","1")
  address = address.replace("二","2")
  address = address.replace("三","3")
  address = address.replace("四","4")
  address = address.replace("五","5")
  address = address.replace("六","6")
  address = address.replace("七","7")
  address = address.replace("八","8")
  address = address.replace("九","9")
  hankaku_address = jaconv.z2h(address, kana=False, ascii=True, digit=True)
  if "丁目" in hankaku_address:
    address1 = hankaku_address.replace("丁目","-")
    if "番地" in hankaku_address:
      address2 = address1.replace("番地","")
    elif "番" in address:
      address2 = address1.replace("番","")
    else:
      address2 = address1
  else:
    if "番地" in hankaku_address:
      address2 = hankaku_address.replace("番地","")
    elif "番" in hankaku_address:
      address2 = hankaku_address.replace("番","")
    else:
      address2 = hankaku_address
  return address2














