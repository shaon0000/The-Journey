$(document).ready(function() {
	teams = [
		{
			name: "The Journey",
			members: ["akb","duncan","krall","shaon"],
			description: "AWESOMENESS"
		},
		{
			name: "The Quitness",
			members: ["derwiki", "neil"],
			description: "We quit."
		}
	]
	
	for (var i=0; i<teams.length; i++) {
		team = teams[i];
		sMembers = team.members.join(', ');
		$(ballot).append(
			$('<div class="team" />')
				.append($('<div class="teamname"/>').text(team.name))
				.append($('<div class="members"/>').text(team.members.join(', ')))
				.append($('<div class="description" />').text(team.description))
				.append($('<div class="useful" />'))
				.append($('<div class="funny" />'))
				.append($('<div class="cool" />'))
				.append($('<div class="bling" />'))
		)
	}

	$('.useful, .funny, .cool, .bling').append($('<div class="rating stars-0" />'))
	ratings = $('.rating')
	for (var i=1; i<=5; i++) {
		(function(i) {
			ratings.append(function(ixRating) {
				console.log('rchoeurchoeurch '+i)
				return $('<div class="starArea"></span>')
					.mouseenter(function(event) {
						console.log('enter')
						$(ratings[ixRating]).addClass('mouseover-stars'+i)
					})
					.mouseleave(function(event) {
						console.log('leave')
						$(ratings[ixRating]).removeClass('mouseover-stars'+i)
					})
					.mouseup(function(event) {
						console.log('click')
						$(ratings[ixRating]).removeClass('stars-1 stars-2 stars-3 stars-4 stars-5').addClass('stars-'+i)
					})
			})
		}(i))
	}
})