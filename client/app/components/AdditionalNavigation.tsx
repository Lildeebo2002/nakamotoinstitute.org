import clsx from "clsx";

export type AdditionalNavigationProps = {
  bottom?: boolean;
  children: React.ReactNode;
};

export async function AdditionalNavigation({
  bottom = false,
  children,
}: AdditionalNavigationProps) {
  return (
    <nav
      aria-label="additional"
      className={clsx(
        "border-dashed border-dark py-3",
        bottom ? "border-t" : "border-b",
      )}
    >
      {children}
    </nav>
  );
}
