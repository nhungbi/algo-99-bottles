def bottle_song(bottle = 99):
	
    if bottle == 1:
        end = """1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""
        return end

    current = f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.\n" + f"Take one down and pass it around, {bottle-1} bottles of beer on the wall.\n"
    return current + bottle_song(bottle-1)

    #while bottle > 2:
        #yield f"{bottle} bottles of beer on the wall, {bottle} bottles of beer."
        #bottle -= 1
        #yield f"Take one down and pass it around, {bottle} bottles of beer on the wall."

    #end = """Take one down and pass it around, 1 bottle of beer on the wall.
	#1 bottle of beer on the wall, 1 bottle of beer.
	#Take one down and pass it around, no more bottles of beer on the wall.
	#No more bottles of beer on the wall, no more bottles of beer.
	#Go to the store and buy some more, 99 bottles of beer on the wall.
	# """
    # yield end

print(bottle_song(10))
