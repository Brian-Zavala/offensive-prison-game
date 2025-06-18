import streamlit as st


def create_prison():
    """Creates the festering shithole you'll call home."""
    prison_map = {
        "your cell": {
            "description": "A tattered, ugly, stinky, shit-caked 6x6 hole. The air is thick with the smell of despair and unwashed asses. This is your life now.",
            "exits": {"cell door": "the block"},
        },
        "the block": {
            "description": "A long, piss-smelling hallway lined with the cages of other miserable bastards. The fluorescent lights hum and flicker, barely cutting through the grime.",
            "exits": {"south": "the yard", "north": "your cell"},
        },
        "the yard": {
            "description": "A concrete square of pure fucking misery under a grey sky. Full of jacked-up psychos looking for a new plaything. You can almost taste the violence in the air.",
            "exits": {"south": "the shiv-eteria", "north": "the block"},
        },
        "the shiv-eteria": {
            "description": "A goddamn feeding trough. The food is a grey slurry of regret and pig anuses. Every meal is a gamble for your teeth and your asshole.",
            "exits": {
                "north": "the yard",
                "east": "the shitter",
                "west": "the grease trap",
            },
        },
        "the shitter": {
            "description": "A foul-smelling chamber of horrors. The toilets are overflowing, and the walls are decorated with things you'd rather not identify. Don't touch anything.",
            "exits": {"west": "the shiv-eteria"},
        },
        "the grease trap": {
            "description": "The prison kitchen. A symphony of boiling fat, rotting food, and the crushed souls of the kitchen staff. You might find a weapon, or you might find dysentery.",
            "exits": {"east": "the shiv-eteria"},
        },
    }
    return prison_map


def display_location(location_name, prison_map):
    """Shows you where the fuck you are."""
    if location_name in prison_map:
        current_location = prison_map[location_name]
        st.subheader(f"Location: {location_name.upper()}")
        st.markdown("---")
        st.write(current_location["description"])
        st.write("**Ways to fuck off from here:**")
        for direction, destination in current_location["exits"].items():
            st.write(f"- Go {direction.capitalize()} to the {destination.capitalize()}")
    else:
        st.error(f"What the shit? '{location_name}' ain't a real place, dumbass.")


def move_player(current_location, direction, prison_map):
    """Drags your pathetic ass to the next shithole."""
    if current_location in prison_map:
        exits = prison_map[current_location]["exits"]
        if direction in exits:
            return exits[direction]
        else:
            st.error("Are you blind, you stupid fuck? You can't go that way.")
            return current_location
    else:
        st.error(
            f"How the hell did you end up in '{current_location}'? That place doesn't exist. Game's fucked."
        )
        return current_location


def main():
    """Main app logic for the miserable prison game."""
    st.set_page_config(page_title="Asshole of the Earth Prison Game", page_icon="🔒")

    # Initialize session state
    if "current_location" not in st.session_state:
        st.session_state.current_location = "your cell"
        st.session_state.prison = create_prison()

    # Game introduction
    st.title("WELCOME TO THE ASSHOLE OF THE EARTH PRISON GAME")
    st.markdown("---")
    st.write("You're scum. The world spat you out, and this is where you landed.")
    st.write(
        "Click a direction button to haul your ass somewhere else, or type 'quit' to give up, you sniveling coward."
    )

    # Display current location
    display_location(st.session_state.current_location, st.session_state.prison)

    # Input for commands
    if st.session_state.current_location == "your cell":
        command_prompt = "You're rotting in your cell. Enter a direction (e.g., 'cell door') or 'jerk off' and cry. Your move, maggot:"
    else:
        command_prompt = (
            "What do you want to do now, you sorry piece of shit excuse of a human?"
        )

    command = st.text_input(command_prompt, key="command_input").lower().strip()

    # Navigation buttons
    current_exits = st.session_state.prison[st.session_state.current_location]["exits"]
    cols = st.columns(len(current_exits))
    for idx, (direction, destination) in enumerate(current_exits.items()):
        with cols[idx]:
            if st.button(f"Go {direction.capitalize()}"):
                st.session_state.current_location = move_player(
                    st.session_state.current_location,
                    direction,
                    st.session_state.prison,
                )

    # Handle text input
    if command:
        if command == "quit":
            st.write("You cowardly piece of shit. Game over.")
            st.session_state.current_location = "your cell"  # Reset game
        elif command in current_exits:
            st.session_state.current_location = move_player(
                st.session_state.current_location, command, st.session_state.prison
            )
        elif command == "jerk off" and st.session_state.current_location == "your cell":
            st.write("You pathetic fuck. You stay in your cell, wallowing in misery.")
        else:
            st.error("Invalid command, dumbass. Try a direction or 'quit'.")


if __name__ == "__main__":
    main()
