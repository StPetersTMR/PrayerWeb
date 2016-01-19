angular.module('prayerApp', [])
	.controller('PrayerListController', function() {
		var prayerList = this;
		prayerList.prayers = [
		    {
		        "topic": "Test Prayer",
		        "description": "Test for prayer system",
		        "date": "2015-05-10"
		    },
		    {
		        "topic": "Test Prayer 2",
		        "description": "Test for prayer system",
		        "date": "2015-05-11"
		    },
		    {
		        "topic": "Pray for Harmonia",
		        "description": "They have practice this day",
		        "date": "2015-05-12"
		    },
		    {
		        "topic": "Midweek Blues",
		        "description": "Pray for those having a bad week, as it is Wednesday",
		        "date": "2015-05-13"
		    },
		    {
		        "topic": "Test Prayer",
		        "description": "This was yesterday...",
		        "date": "2015-05-14"
		    },
		    {
		        "topic": "Test Prayer Today",
		        "description": "Today's Prayer",
		        "date": "2015-05-15"
		    },
		    {
		        "topic": "Last day",
		        "description": "A Saturday",
		        "date": "2015-05-16"
		    },
		    {
		        "topic": "Old day",
		        "description": "Some time in the past",
		        "date": "2015-05-01"
		    },
		    {
		        "topic": "url test",
		        "description": "Future test for markdown (interpretation)[https://blog.draringi.net]",
		        "date": "2015-05-21"
		    },
		    {
		        "topic": "BSDCan",
		        "description": "Pray that BSDCan goes well",
		        "date": "2015-06-08"
		    },
		    {
		        "topic": "Today test",
		        "description": "Another Today\r\nWith\r\nMultiple\r\nLines?",
		        "date": "2015-05-17"
		    },
		    {
			"topic": "November test",
                        "description": "I'm testing this on November 1st",
                        "date": "2015-11-01"
                    },
		    {
			"topic": "Christmas Eve",
			"description": "Christmas Eve Test",
			"date": "2015-12-24"
		    }
		];
		prayerList.index = 3;
		prayerList.current = prayerList.prayers[prayerList.index];
		prayerList.next = function () {
			if (prayerList.index < prayerList.prayers.length - 1) {
				prayerList.index++;
				prayerList.updatePage();
			}
		};
		prayerList.prev = function () {
			if (prayerList.index > 0){
				prayerList.index--;
				prayerList.updatePage();
			}
		};
		prayerList.updatePage = function () {
			prayerList.current = prayerList.prayers[prayerList.index];
			prayerList.setNext();
			prayerList.setPrev();
		};
		prayerList.setNext = function () {
			if (prayerList.index < prayerList.prayers.length - 1) {
				prayerList.nextClass = "";
			} else {
				prayerList.nextClass = "disabled"
			};
		};
		prayerList.setPrev = function () {
			if (prayerList.index > 0) {
				prayerList.prevClass = "";
			} else {
				prayerList.prevClass = "disabled";
			};
		};
		prayerList.updateToday = function () {
			prayerList.today = new Date();
		};
		prayerList.gotoDate = function (date) {
			date_string = date.getFullYear() +  "-" + (date.getMonth()+1) + "-" + date.getDate()
			prayerList.index = prayerList.prayers.findIndex(function(o){
				if(o.date == date_string){
					return true;
				} else {
					return false;
				}
			});
			prayerList.updatePage();
		}
		prayerList.gotoToday = function () {
			prayerList.updateToday();
			prayerList.gotoDate(prayerList.today);
		}
		prayerList.today = new Date();
		prayerList.nextClass = "";
		prayerList.prevClass = "";
	});
