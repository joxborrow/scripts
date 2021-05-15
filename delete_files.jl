for (root, dirs, files) in walkdir(".")
    print("Directories in $root")
    for dir in dirs
        println(joinpath(root, dir))
    end
    println("Files in $root")
    for file in files
        println(joinpath(root, file))
    end
end