class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name.lower()
        self.__source=source.lower()
        self.__destination=destination.lower()
        self.__ticket_id=None
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_ticket_id(self):
        return self.__ticket_id
    def validate_source_destination(self):
       if (self.__source == "delhi"):
           if self.__destination=="mumbai":
               return True
           elif self.__destination=="chennai":
               return True
           elif self.__destination=="pune":
               return True
           elif self.__destination=="kolkata":
               return True
           else:
               return False
       else:
           return False        
    def  generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            if Ticket.counter<10:
                self.ticket_id=self.source[0] + self._destination[0] + str(0) + str(Ticket.counter)
            else:
                self.__ticket_id=self.source[0] + self._destination[0] + str(Ticket.counter)
            return self.__ticket_id.upper()
        else:
            self.__ticket_id=None
T1=Ticket("sniota","delhi","mumbai")
T2=Ticket("sniper","delhi","pune")
print(T1.generate_ticket())
print(T2.generate_ticket())
