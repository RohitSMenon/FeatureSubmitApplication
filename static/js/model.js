
function request(data) {
    this.id = ko.observable(data.request_id);
    this.title = ko.observable(data.title);
    this.description = ko.observable(data.description);
    this.client = ko.observable(data.client);
    this.clientPriority = ko.observable(data.clientPriority);
    this.targetDate = ko.observable(data.targetDate);
    this.productArea = ko.observable(data.productArea);
    }

function AppViewModel()
{
    this.showMe = ko.observable(false); 
self.requests = ko.observableArray([]);
this.title=ko.observable("");
this.description=ko.observable("");
this.client=ko.observable();
this.clients = ko.observableArray
([
'Client A','Client B','Client C'
]);

this.clientPriority=ko.observable();
this.priority= ko.observableArray
([
'1','2','3'
]);
this.targetDate=ko.observable("");
this.productArea=ko.observable();
this.products= ko.observableArray
([
'Policies','Billing', 'Claims', 'Reports'
]);

this.submit=function()
{
    alert("heresds");
    var data=ko.toJSON(this);
    $.post("/requestSubmit",
    data, function(retData)
    {
    alert("here >> "+retData);
    });

}
this.getData=function()
{
    this.showMe(true);
    alert("getData");
    var data=ko.toJSON(this);
    $.getJSON("/getRequests", function(retData) { 
        alert(retData);
        var mappedTasks = $.map(retData, function (item) { return new request(item) });
        self.requests(mappedTasks);
    })

}

};


// Activates knockout.js q`

ko.applyBindings(new
AppViewModel());



