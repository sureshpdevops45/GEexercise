SO="stackover flow"
echo -n $SO | wc -c
SO="stackover flow"
echo -n $SO | wc -w

grep -o "o" <<<"$SO" | wc -l