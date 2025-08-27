export type Element = {
  name: string;
  xpath: string;
  url: string;
  typeSelector?: string; // "text", "href", "src", "alt", etc.
};
