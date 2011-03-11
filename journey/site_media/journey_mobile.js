$(document).ready(function() {
	teams = [
		{
			name: "The Journey",
			members: ["akb","duncan","krall","shaon"],
			description: "AWESOMENESS",
			stats: {
				useful: 1,
				funny: 5,
				cool: 3,
				bling: 2
			}
		},
		{
			name: "The wattt",
			members: ["jeff", "jim"],
			description: "Wat.",
			stats: {
				useful: 3,
				funny: 4,
				cool: 5,
				bling: 1
			}
		}
	]
	
	for (var i=0; i<teams.length; i++) {
		team = teams[i];
		sMembers = team.members.join(', ');
		var team_votes = $('<div class="team_votes" style="display:none"/>');
		var labels_and_scores = [["Useful", team.stats.useful], ["Funny", team.stats.funny ], ["Cool", team.stats.cool], ["Bling", team.stats.bling]];

		$.each(labels_and_scores, function(event, node) {
			var rating_container = $('<div class="rating-container" />');
			var label_container = $('<div class="type-desc />').append($("<span />").text(node[0]));
			var rating = $('<div class="rating stars-'+node[1]+'" />');
			rating_container.append(label_container);
			rating_container.append(rating);
			team_votes.append(rating_container);
		    });

		var team_desc = $('<div class="team-description" />')
			.append($('<div class="col1 teamname"/>').text(team.name))
			.append($('<div class="col2 members"/>').text(team.members.join(', ')))
			.append($('<div class="col3 description" />').text(team.description))

		$('#hackathon-teams').append(
			$('<div class="team" />')
			.append(team_desc)
			.append(team_votes)
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

	$(".team-description").click(function(){
		$(this).next().slideToggle();
	    });
})


