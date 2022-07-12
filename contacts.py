class ContactDetails:
  def __init__(self,contactDetailsId , contactType, contactDetail):
    self.contactDetailsId = contactDetailsId
    self.contactType = contactType
    self.contactDetail = contactDetail 
  @staticmethod 
  def createContactDetails(contactDetailsId , contactType, contactDetail):
    return Contacts(contactDetailsId , contactType, contactDetail)

class User:
  def __init__(self, userId , fName , lName , isAdmin , isActive , contacts):
    self.userId = userId
    self.fName = fName
    self.lName = lName 
    self.isAdmin = isAdmin
    self.isActive = isActive
    self.contacts = contacts

  @staticmethod
  def createAdmin(userId , fName , lName , contacts):
    return User(userId , fName , lName , True , True , contacts)

  def createStaff(self , userId , fName , lName , contacts):
    if(self.isAdmin == True):
      return User(userId , fName , lName , False , True , contacts)
    else :
      return "You Dont Have Admin Access"

  def updateStaff(self , obj , name , value):
    if(self.isAdmin == True):
      setattr(obj , name , value)
    else :
      return "You dont have the permission to Update"

  def readStaff(self , obj):
    if(self.isAdmin == True):
      return obj.userId + " " + obj.fName + "_" + obj.lName 
    else :
      return "You dont have admin access"
  
  def deleteStaff(self , obj):
    if(self.isAdmin == True):
      obj.isActive = False
    else :
      return "You dont have admin access"

  def createContact(self , contactId , fName , lName  , contactDetailsId , contactType, contactDetail):
    contactObject = Contacts.createContact(contactId , fName , lName , contactDetailsId , contactType, contactDetail)
    self.contacts.append(contactObject)

         
  def readContact(self, index):
    if not self.isActive:
      print("The account has been deleted")
      return
    contact = self.contacts[index]
    print(contact.fName, contact.lName, contact.contactDetails)



  def updateContact(self, contactName, propertyName, newValue):
    if not self.isActive:
      print("You are not active! You cannot update a contact.")
      return
    setattr(contactName, propertyName, newValue)
    return "The contact has been updated"


  def deleteContact(self, index):
    if not self.isActive:
      print("You are not active! You cannot delete a contact.")
      return
    self.contacts.pop(index)


  def createContactDetail(self, index, contactDetail):
    if not self.isActive:
      print("The account has been deleted")
      return
    self.contacts[index].contactDetails.append(contactDetail)

  def readContactDetail(self, contactIndex, detailIndex):
    if not self.isActive:
      print("The account has been deleted")
      return
    detail = self.contacts[contactIndex].contactDetails[detailIndex]
    print(detail.detailId, detail.detailType, detail.contactDetail)

  def updateContactDetail(self, contactIndex, detailIndex, propertyName, newValue):
    if not self.isActive:
      print("The account has been deleted")
      return
    detail = self.contacts[contactIndex].contactDetails[detailIndex]
    setattr(detail, propertyName, newValue)

  def deleteContactDetail(self, contactIndex, detailIndex):
    if not self.isActive:
      print("You are not active! You cannot delete a contact detail.")
      return
    self.contacts[contactIndex].contactDetails.pop(detailIndex)

class Contacts:
  def __init__(self , contactId , fName , lName , isActive , contactDetails):
    self.contactId = contactId 
    self.fName = fName
    self.lName = lName
    self.isActive = isActive
    self.contactDetails = contactDetails
  
  @staticmethod
  def createContact(contactId , fName , lName , contactDetailsId , contactType, contactDetail):
    contactDetails = ContactDetails.createContactDetails(contactDetailsId , contactType, contactDetail)
    return Contacts(contactId , fName , lName , contactDetails)
