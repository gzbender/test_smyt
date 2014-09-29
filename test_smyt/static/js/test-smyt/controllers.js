var testSmytControllers = angular.module('testSmytControllers', []);

testSmytControllers.controller('ObjectListCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        var _editing = [],
            model = $routeParams.model;
        function updateList(){
            $http.get(window.API_URLS.objects.replace(':model', model))
                .success(function(data){
                    $scope.objects = data.objects;
                    $scope.fields = data.fields;
                });
        }
        updateList();
        $scope.newObj = {};
        $scope.edit = function(objectId, field){
            if(_editing && !angular.equals(_editing, [objectId, field])){
                for(var i=0; i<$scope.objects.length; i++){
                    var obj = $scope.objects[i];
                    if(obj.id === _editing[0]){
                        var data = {};
                        data[_editing[1]] = obj[_editing[1]];
                        $http({
                            method: 'PATCH',
                            url: window.API_URLS.update_object
                            .replace(':model', model)
                            .replace(':id', obj.id),
                            data: data})
                            .error(function(){
                                updateList();
                            });
                    }
                }
            }
            _editing = [objectId, field];
        }
        $scope.isEdit = function(objectId, field){
            return angular.equals(_editing, [objectId, field]);
        }
        $scope.create = function(){
            $http.post(window.API_URLS.create_object.replace(':model', model), $scope.newObj)
                .success(function(data){
                    $scope.newObj = {};
                    $scope.objects.push(data);
                })
        }
}]);