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
			var team_votes = $('<div class="team_votes" style="display:none"/>');
			var labels_and_scores = [["Useful", team.stats.USEFUL], ["Funny", team.stats.FUNNY ], ["Cool", team.stats.COOL], ["Bling", team.stats.BLING]];

			$.each(labels_and_scores, function(index, label_and_score) {
				var rating_container = $('<div class="rating-container" />');
				var label_container = $('<div class="type-desc" />').append($("<span />").text(label_and_score[0]));
				var rating = $('<div class="rating stars-'+label_and_score[1]+'" />');
				rating_container.append(label_container);
				rating_container.append(rating);
				rating_container.attr('votetype',label_and_score[0].toUpperCase())
				team_votes.append(rating_container);
			    });

			var team_desc = $('<div class="team-description" />')
				.append($('<div class="col1 teamname"/>').text(team.name))
				.append($('<div class="col2 members"/>').text(team.members.join(', ')))

			$('#hackathon-teams').append(
				$('<div class="team" />')
				.attr('teamnum', team.project_id)
				.append(team_desc)
				.append(team_votes)
			)
		}

		ratings = $('.rating')
		for (var i=1; i<=5; i++) {
			(function(i) {
				ratings.append(function(ixRating) {
					var starArea = $('<div class="starArea"></span>')
					starArea.click(function (event) {
						$(ratings[ixRating]).removeClass('stars-1 stars-2 stars-3 stars-4 stars-5').addClass('stars-'+i)
						project_id = $(event.target).parents('.team').attr('teamnum')
						vote_type = $(event.target).parents('.rating-container').attr('votetype')
						$.post('/vote/', {
							project_id: project_id,
							vote_type: vote_type,
							score: i
						})
					});
					return starArea;
				});
			}(i))
		}

		$(".team-description").click(function(){
			$('.team-description').next().slideUp();
			$(this).next().slideDown();
		    });
	}

}());