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
				$('<div class="team" id="team-'+team.project_id+'" teamnum="'+team.project_id+'"/>')
					.append($('<div class="teamname"/>').text(team.name))
					.append($('<div class="members"/>').text(team.members.join(', ')))
					.append($('<div class="ufcb" votetype="USEFUL" />').append($('<div class="rating stars-'+team.stats.USEFUL+'" />')))
					.append($('<div class="ufcb" votetype="FUNNY" />').append($('<div class="rating stars-'+team.stats.FUNNY+'" />')))
					.append($('<div class="ufcb" votetype="COOL" />').append($('<div class="rating stars-'+team.stats.COOL+'" />')))
					.append($('<div class="ufcb" votetype="BLING" />').append($('<div class="rating stars-'+team.stats.BLING+'" />')))
			)
		}

		ratings = $('.rating')
		for (var i=1; i<=5; i++) {
			(function(i) {
				ratings.append(function(ixRating) {
					var starArea = $('<div class="starArea"></span>')
					if (!mobile) {
						starArea
							.mouseenter(function(event) {
								$(ratings[ixRating]).addClass('mouseover-stars'+i)
							})
							.mouseleave(function(event) {
								$(ratings[ixRating]).removeClass('mouseover-stars'+i)
							});
					}
					starArea.click(function (event) {
						$(ratings[ixRating]).removeClass('stars-1 stars-2 stars-3 stars-4 stars-5').addClass('stars-'+i)
						project_id = $(event.target).parents('.team').attr('teamnum')
						vote_type = $(event.target).parents('.ufcb').attr('votetype')
						$.post('/vote/', {
							project_id: project_id,
							vote_type: vote_type,
							score: i
						})
					});
					return starArea;
				})
			}(i))
		}
	}



}());