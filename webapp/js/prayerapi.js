var prayerAPI = angular.module('prayerAPI', ['ngResource']);

prayerAPI.factory('PrayerTopic', ['$resource',
	function($resource){
		return $resource('/prayerapp/topics/:id/', {}, {
			query: {method:'GET', isArray:true}
		});
}]);
