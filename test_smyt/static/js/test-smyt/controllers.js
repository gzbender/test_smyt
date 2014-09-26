var testSmytControllers = angular.module('testSmytControllers', []);

testSmytControllers.controller('ObjectListCtrl', ['$scope', '$routeParams',
    function($scope, $routeParams){
        var _editing = [],
            maxId = 5,
            model = $routeParams.model;
        $scope.newObj = {};
        $scope.inputTypes = {
            int: 'number',
            char: 'text',
            date: 'date'
        }
        if(model == 'Users'){
            $scope.objectList = [{
                id: 3,
                text: "dfgd",
                cnt: 15,
                date: '12-02-2014'
            },{
                id: 5,
                text: "yujy",
                cnt: 17,
                date: '20-06-2014'
            }];
        }
        else{
            $scope.objectList = [{
                id: 3,
                text: "dfgdgfhf",
                cnt: 15,
                date: '12-02-2014'
            },{
                id: 5,
                text: "35erfdf35",
                cnt: 17,
                date: '20-06-2014'
            },{
                id: 7,
                text: "dfgdgfhf",
                cnt: 15,
                date: '12-02-2014'
            },{
                id: 10,
                text: "35erfdf35",
                cnt: 17,
                date: '20-06-2014'
            }];
        }
        $scope.fields = [{
            name: 'id',
            type: 'int',
            title: 'Id',
            editable: false
        }, {
            name: 'text',
            type: 'char',
            title: 'Title',
            editable: true
        }, {
            name: 'cnt',
            type: 'int',
            title: 'Count',
            editable: true
        }, {
            name: 'date',
            type: 'date',
            title: 'Date',
            editable: true
        }];
        $scope.edit = function(objectId, field){
            _editing = [objectId, field];
        }
        $scope.isEdit = function(objectId, field){
            return angular.equals(_editing, [objectId, field]);
        }
        $scope.create = function(){
            var obj = {
                id: ++maxId
            };
            for(var key in $scope.newObj){
                obj[key] = $scope.newObj[key];
            }
            $scope.objectList.push(obj);
            $scope.newObj = {};
        }
}]);