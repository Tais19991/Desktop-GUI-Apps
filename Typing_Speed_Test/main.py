from window_manager import MainWindow
from timer import Timer
from text_manager import TextManager

window = MainWindow()
text = TextManager("text.txt")
timer = Timer()

# Read text file and upload example text on canvas
text.read_text_file()
window.prepare_text_to_fit_canvas_width(text.text_list)
uploaded_text = window.place_text_on_canvas()
text.get_example_text(uploaded_text)


def set_timer() -> None:
    """Manage countdown timer, update UI, and display results when time is up."""
    if timer.work_sec >= 0:
        min, sec = timer.count_down()
        window.update_timer_label(min, sec)
        window.timer_label.after(1000, set_timer)
    else:
        timer.reset_timer()
        window.reset_timer_label()
        words_in_min, num_all_words, mistakes = text.final_check_user_text()
        window.show_result(words_in_min, num_all_words, mistakes)
        window.user_text_input.config(state='disabled')


def on_click(event) -> None:
    """Clear existing text and start the countdown timer on first click."""
    window.user_text_input.config(state='normal')
    window.user_text_input.delete("1.0", "end-1c")
    window.user_text_input.unbind("<Button-1>")
    set_timer()


def on_key_release(event) -> None:
    """Process user's text input, update the canvas with new text if conditions are met."""
    current_user_text = window.user_text_input.get("1.0", "end-1c")
    text.get_user_text(current_user_text)

    if text.words_uploaded == text.user_words or \
            len(text.words_uploaded) <= len(text.user_words):
        window.clear_text_from_canvas()
        current_text = window.place_text_on_canvas()
        text.get_example_text(current_text)


def reset() -> None:
    """Reset the timer, UI labels, text manager, and widgets to initial states."""
    timer.reset_timer()
    window.reset_timer_label()
    text.reset_text_manager()
    window.reset_widgets(on_click)
    text.get_example_text(uploaded_text)


# Buttons and actions
window.restart_button.config(command=reset)
window.user_text_input.bind("<Button-1>", on_click)
window.user_text_input.bind("<KeyRelease>", on_key_release)

if __name__ == "__main__":
    window.mainloop()
