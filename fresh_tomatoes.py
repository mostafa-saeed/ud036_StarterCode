import webbrowser
import os

# Read and return the content of a template file
def read_template_file(filename):
    TEMPLATE_PATH = "templates/" + filename
    file_reader = open(TEMPLATE_PATH, "r")
    return file_reader.read()

# The main page layout and title bar
main_page_content = read_template_file('main_page_content.html')
# A single movie entry html template
movie_tile_content = read_template_file('movie_tile_content.html')

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_id,
            movie_story=movie.story.encode('utf-8').strip()
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('public/index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)