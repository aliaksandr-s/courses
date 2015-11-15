var bio = {
	"name" : "Homer Simpson",
	"role" : "WebDeveloper",
	"welcomeMessage" : 'Homer is one of the most influential characters in the history of television. The British newspaper The Sunday Times described him as "the greatest comic creation of [modern] time". He was named the greatest character "of the last 20 years" in 2010 by Entertainment Weekly, was ranked the second greatest cartoon character by TV Guide, behind Bugs Bunny, and was voted the greatest television character of all time by Channel 4 viewers. For voicing Homer, Castellaneta has won four Primetime Emmy Awards for Outstanding Voice-Over Performance and a special-achievement Annie Award. In 2000, Homer and his family were awarded a star on the Hollywood Walk of Fame.',
	"image" : "images/homer-simpson.jpg",
	"contacts" : [{
		"mobile" : "555-55-55",
		"twitter" : "H-Simpson",
		"location" : "Springfield",
		"email" : "H-Simpson@gmail.com"
	}],
	"skills" : ["Sense of humour","Confidence","Musical tallent","Polyglot"]
};

var work = {
	"jobs" : [
	{
		"employer" : "Springfield Power Company",
		"title" : "Technical Supervisor",
		"dates" : "2010 - 2013",
		"location" : "New York",
		"description" : "Homer rarely attends his job, and yet hardly gets fired, and always has his job waiting for him when he wants to return."
	},
	{
        "employer" : "Springfield Power Company",
		"title" : "Safety Inspector",
		"dates" : "2013 - 2015",
        "location" : "Paris",
		"description" : "On one occasion, Homer has misinterpreted a threat about losing his job as a hint that he can take the next day off."
	}]
};

var projects = {
	"project" : [{
		"title" : "Homer's Beer",
		"dates" : "2013",
		"description" : "The greatest Beer in the world",
		"images" : ["images/1.jpg","images/2.jpg","images/3.jpg","images/4.jpg"]
	},
	{
        "title" : "Homer's Beer 2",
		"dates" : "2014",
        "description" : "The greatest Beer in the world improved version",
		"images" : ["images/1.jpg","images/2.jpg","images/3.jpg","images/4.jpg"]
	}]
};

var education = {
	"schools" : [
	{
		"name" : "Springfield school",
		"location" : "Springfield",
		"degree" : "bachelor",
		"majors" : "computer science",
		"dates" : "1990 - 2000",
		"url" : "spring.scl.com"
	},
	{
        "name" : "Springfield University",
		"location" : "Springfield",
		"degree" : "master",
		"majors" : "computer science",
		"dates" : "2000 - 2005",
        "url" : "spring.unv.com"
	}],
	"online courses" : [{
		"title" : "Front-End Web Developer Nanodegree",
		"school" : "udacity",
		"dates" : "2014 - 2015",
		"url" : "https://www.udacity.com/course/nd001"
	}]
};

bio.display = function() {
	var formattedName = HTMLheaderName.replace("%data%",bio.name);
	var formattedRole = HTMLheaderRole.replace("%data%",bio.role);
	var formattedImage = HTMLbioPic.replace("%data%",bio.image);
	var formattedMessage = HTMLwelcomeMsg.replace("%data%",bio.welcomeMessage);

	$("#header").prepend(formattedRole).prepend(formattedName).append(formattedImage,formattedMessage);
	$("#header").append(HTMLskillsStart);

	for(skill in bio.skills) {
		var formattedSkills = HTMLskills.replace("%data%",bio.skills[skill]);
		$("#skills").append(formattedSkills);
	};

	for(contact in bio.contacts) {
		var formattedMobile = HTMLmobile.replace("%data%",bio.contacts[contact].mobile);
		var formattedEmail = HTMLemail.replace("%data%",bio.contacts[contact].email);
		var formattedTwitter = HTMLtwitter.replace("%contact%","skype").replace("%data%",bio.contacts[contact].twitter);
		$("#footerContacts").append(formattedMobile,formattedEmail,formattedTwitter);
	};
};

work.display = function () {
    for (job in work.jobs){
        $("#workExperience").append(HTMLworkStart);

        var formatedEmployer = HTMLworkEmployer.replace('%data%', work.jobs[job].employer);
        var formatedTitle = HTMLworkTitle.replace('%data%', work.jobs[job].title);
        var formatedDates = HTMLworkDates.replace('%data%', work.jobs[job].dates);
        var formatedLocation = HTMLworkLocation.replace('%data%', work.jobs[job].location);
        var formattedDescription = HTMLworkDescription.replace("%data%",work.jobs[job].description);

        $(".work-entry:last").append(formatedEmployer + formatedTitle, formatedDates, formatedLocation, formattedDescription);
    };
};

projects.display = function () {
	for (item in projects.project){
		$('#projects').append(HTMLprojectStart);

		var formattedTitle = HTMLprojectTitle.replace("%data%",projects.project[item].title);
		var formattedDates = HTMLprojectDates.replace("%data%",projects.project[item].dates);
		var formattedDescription = HTMLprojectDescription.replace("%data%",projects.project[item].description);

		$(".project-entry:last").append(formattedTitle,formattedDates,formattedDescription);
		for (image in projects.project[item].images){
			var formattedImage = HTMLprojectImage.replace("%data%", projects.project[item].images[image]);
			$(".project-entry:last").append(formattedImage);
		}
	};
};

education.display = function() {
	for(school in education.schools) {
		$("#education").append(HTMLschoolStart);

		var formattedName = HTMLschoolName.replace("%data%",education.schools[school].name);
		var formattedDegree = HTMLschoolDegree.replace("%data%",education.schools[school].degree);
		var formattedDates = HTMLschoolDates.replace("%data%",education.schools[school].dates);
		var formattedLocation = HTMLschoolLocation.replace("%data%",education.schools[school].location);
		var formattedUrl = HTMLonlineURL.replace("%data%",education.schools[school].url);
		$(".education-entry:last").append(formattedName + formattedDegree,formattedDates,formattedLocation,formattedUrl);
	};
	for(course in education['online courses']){
		$("#education").append(HTMLonlineClasses);
		$("#education").append(HTMLschoolStart);

		var formattedHTMLonlineTitle = HTMLonlineTitle.replace("%data%",education['online courses'][course].title);
		var formattedHTMLonlineSchool = HTMLonlineSchool.replace("%data%",education['online courses'][course].school);
		var formattedHTMLonlineDates = HTMLonlineDates.replace("%data%",education['online courses'][course].dates);
		var formattedHTMLonlineURL = HTMLonlineURL.replace("%data%",education['online courses'][course].url);
		$(".education-entry:last").append(formattedHTMLonlineTitle + formattedHTMLonlineSchool, formattedHTMLonlineDates, formattedHTMLonlineURL);
	}
};

work.display();
bio.display();
projects.display();
education.display();



// Click location function

// $(document).click(function(loc) {
//   var xCoord = loc.clientX;
//   var yCoord = loc.clientY;
//   console.log(xCoord, yCoord, loc);
// });



// InternationalizeName function



function inName(name) {
	console.log(name);
	var splittedName = name.split(' ');
	var firstName = splittedName[0];
	var lastName = splittedName[1];

	firstName = firstName[0].toUpperCase() + firstName.slice(1).toLowerCase();
	lastName = lastName.toUpperCase();
	return(firstName+ " " +lastName);

};

$("#mapDiv").append(googleMap);
$('#main').append(internationalizeButton);
