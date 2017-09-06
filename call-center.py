class Call(object):
    id_number = 1
    def __init__(self,name,phone_number,time_to_call,reason):
        self.id_number = Call.id_number
        self.name = name
        self.phone_number = phone_number
        self.time_to_call = time_to_call
        self.reason = reason
        Call.id_number += 1
    def display(self):
        print "ID: #" + str(self.id_number)
        print "Name: " + str(self.name)
        print "Phone Number: " + str(self.phone_number)
        print "Time to Call: " + str(self.time_to_call)
        print "Reason for Call: " + str(self.reason)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self,call):
        self.calls.append(call)
        return self
    def remove(self):
        del self.calls[0]
        return self
    def info(self):
        for call in self.calls:
            print "Name: " + str(call.name)
            print "Phone Number: " + str(call.phone_number)
        print "Queue length is " + str(len(self.calls))
        return self


caller_1 = Call("Nathan","(555)555-5555","2:00pm","Wanted to")
caller_2 = Call("Sarah","(555)555-5555","4:00pm","Needed to")
caller_3 = Call("Tyler","(555)555-5555","2:00pm","Wanted to")
caller_4 = Call("Rose","(555)555-5555","4:00pm","Needed to")

CallCenter().add(caller_1).add(caller_2).add(caller_3).add(caller_4).info()