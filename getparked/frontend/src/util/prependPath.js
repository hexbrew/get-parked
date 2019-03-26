export default string => {
  const element = document.getElementById("path");

  if (!element) {
    return string;
  }

  return `/${element.dataset.path}${string}`;
};
