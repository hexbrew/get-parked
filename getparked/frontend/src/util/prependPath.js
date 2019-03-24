export default (string) => {
  const path = document.getElementById('path').dataset.path;
  return (`/${path}${string}`)
}