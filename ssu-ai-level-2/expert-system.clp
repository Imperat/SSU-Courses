(deffunction ask-question (?question $?allowed-values)
    (printout t ?question)
    (bind ?answer (read))

    (if (lexemep ?answer) then
        (bind ?answer (lowcase ?answer)))

    (while (not (member ?answer ?allowed-values)) do
        (printout t ?question)
        (bind ?answer (read))

        (if (lexemep ?answer) then
            (bind ?answer (lowcase ?answer)))
    )

    ?answer
)
