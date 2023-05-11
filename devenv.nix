{ pkgs, ... }:

{
  packages = [ pkgs.git ];

  languages.python = {
    enable = true;
    poetry = {
      enable = true;
    };
  };
  languages.typescript.enable = true;

  services.postgres.enable = true;
}
