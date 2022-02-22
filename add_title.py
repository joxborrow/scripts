# Add Video Title frames
# =========================================================================
# This program adds a short title clip to a video.
# 
# Dependencies:
# 	movie.editor

import moviepy.editor as me

# Set key parameters
clip_path = r"C:\Users\Owner\Documents\zoom\2022-02-19 19.47.21 Jonathan Oxborrow's Personal Meeting Room\video1219671280.mp4"
clip_title = 'Text Clip'
title_color = 'white'
title_font = 'Arial-Bold'
title_font_size = 100
title_duration = 5
title_fadeout_duration = 1.0
fadein_duration = 2.0
export_path = 'final.mp4'

# Read in the clip
clip = me.VideoFileClip(clip_path)

# Prep the clip
clip = me.vfx.fadein(clip, fadein_duration)

# Create the intro clip
title = me.TextClip(txt=clip_title, color=title_color, font=title_font, fontsize=title_font_size, size=clip.size)
title.duration = title_duration
title = me.vfx.fadeout(title, title_fadeout_duration)

# Combine and export finalized clip
clip_final = me.concatenate_videoclips([title, clip])
clip_final.write_videofile(export_path)
clip_final.close()

