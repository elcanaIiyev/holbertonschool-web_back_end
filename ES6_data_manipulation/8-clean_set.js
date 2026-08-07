export default function cleanSet(set, startString) {
  if (typeof startString !== "string" || startString.length === 0) {
    return "";
  }

  return [...set]
    .filter(
      (value) =>
        typeof value === "string" && value.startsWith(startString)
    )
    .map((value) => value.slice(startString.length))
    .join("-");
}
