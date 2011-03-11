$(document).ready(function() {
	teams = [
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "REally Long TItle for the Project Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "Online Voting",
			members: ["akb","duncan","krall","shaon","shaon","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		
		{
			name: "The Journey",
			members: ["akb","duncan","krall","shaon"],
			description: "Hey YA",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},{
			name: "The Journey",
			members: ["akb","duncan","krall","shaon"],
			description: "This is a really long description. Let's see how far this goes without us getting too much info",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},{
			name: "The Journey",
			members: ["akb"],
			description: "So Cool",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		{
			name: "The Journey",
			members: ["shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},{
			name: "The Journey",
			members: ["akb","duncan","krall","shaon"],
			description: "What What",
			stats: {
				useful: 1,
				funny: 2,
				cool: 3,
				bling: 4
			}
		},
		
	]
	
	for (var i=0; i<teams.length; i++) {
		team = teams[i];
		sMembers = team.members.join(', ');
		$(ballot).append(
			$('<div class="team" />')
				.append($('<div class="teamname"/>').text(team.name))
				.append($('<div class="members"/>').text(team.members.join(', ')))
				.append($('<div class="useful" />').append($('<div class="rating stars-'+team.stats.useful+'" />')))
				.append($('<div class="funny" />').append($('<div class="rating stars-'+team.stats.funny+'" />')))
				.append($('<div class="cool" />').append($('<div class="rating stars-'+team.stats.cool+'" />')))
				.append($('<div class="bling" />').append($('<div class="rating stars-'+team.stats.bling+'" />')))
				
		)
	}

	ratings = $('.rating')
	for (var i=1; i<=5; i++) {
		(function(i) {
			ratings.append(function(ixRating) {
				return $('<div class="starArea"></span>')
					.mouseenter(function(event) {
						$(ratings[ixRating]).addClass('mouseover-stars'+i)
					})
					.mouseleave(function(event) {
						$(ratings[ixRating]).removeClass('mouseover-stars'+i)
					})
					.mouseup(function(event) {
						$(ratings[ixRating]).removeClass('stars-1 stars-2 stars-3 stars-4 stars-5').addClass('stars-'+i)
					})
			})
		}(i))
	}
})