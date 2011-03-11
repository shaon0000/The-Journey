(function() {
	$(document).ready(function() {
		$.ajax('/my_votes', {
			success: showVotes
		})
	});

	function showVotes(teams) {
		for (var i=0; i<teams.length; i++) {
			team = teams[i];
			sMembers = team.members.join(', ');
			$("#ballot").append(
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
	}

}());