boilerplate=$(cat <<EOF
def solution():
    pass

if __name__ == "__main__":
    print(solution())
EOF
)

for i in {1..500}; do
  num=$(printf "%03d" "$i")
  filename="pb_$num.py"
  touch "$filename"
  echo -e "# $filename\n" >> "$filename"
  echo "$boilerplate" >> "$filename"
done
