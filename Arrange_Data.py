class Data_Menu:
  def Data_Menu(dishId, dishName, dishDescription, dishPrice):
    dishId = dishId
    dishName = dishName
    dishDescription = dishDescription
    dishPrice = dishPrice
  pass


def List_Data(data,s):
  # Returns LIST (HashMap) Of the origin they sought the id, name, description and price
  data_Menu=dict({})
  latitude1 = data['Data']['categoriesList']
  t=0;
  ty=0;
  for x in latitude1 :
    latitude2 = data['Data']['categoriesList'][t]['categoryName']
    if (latitude2 == s):
      t3 = data['Data']['categoriesList'][t]['dishList']
      for y in t3:
        #temp = Data_Menu(str(t3[ty]['dishId'] ,t3[ty]['dishName'] ,t3[ty]['dishDescription'] ,str(t3[ty]['dishPrice'])
        s_data = "dishId : "+str(t3[ty]['dishId'])+" dishName : "+t3[ty]['dishName']+", dishDescription : "+t3[ty]['dishDescription']+", dishPrice : "+str(t3[ty]['dishPrice'])
        #print(s_data)
        data_Menu[t3[ty]['dishId']] = s_data
        ty=ty + 1
    t=t+1
  return data_Menu



