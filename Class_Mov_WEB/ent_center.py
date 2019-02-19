import fresh_tomatoes
import media

toy_story = media.movie("Toy Story",
			"A story of a heros with toy",
			"https://www.zeldaspalace.com/images/oot/arts/link-zelda.png",
			"https://www.youtube.com/watch?v=Bj4gS1JQzjk")
avatar_2 = media.movie("avatar 2",
			"A story of a heros with toy",
			"https://www.zeldaspalace.com/images/oot/arts/link_03.png",
			"https://www.youtube.com/watch?v=WbMD53XPJWA")

#print (toy_story.trailer)
#avatar_2.show_trailer()

SCIENCE = media.movie("Scinece",
			"A story of a heros with toy",
			"https://www.zeldaspalace.com/images/oot/arts/3d_Link.png",
			"https://www.youtube.com/watch?v=lK3-NkkHiXc")
comedy = media.movie("comedy",
			"A story of a heros with toy",
			"https://www.zeldaspalace.com/images/oot/arts/3d_LinkEpona.png",
			"https://www.youtube.com/watch?v=RqHI0kE-cyo")

movies = [toy_story, avatar_2, SCIENCE, comedy]
fresh_tomatoes.open_movies_page(movies)
