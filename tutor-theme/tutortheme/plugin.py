import importlib_resources
from tutor import hooks
from tutor.core.hooks import priorities

# Register custom theme templates.
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutortheme") / "templates"),
    priority=priorities.HIGH,
)

# Copy Indigo theme files into the Open edX themes directory.
hooks.Filters.ENV_TEMPLATE_TARGETS.add_item(
    ("indigo", "build/openedx/themes")
)

# Ensure Sass files inside partials directories are included.
hooks.Filters.ENV_PATTERNS_INCLUDE.add_items(
    [
        r"indigo/lms/static/sass/partials/lms/theme/",
        r"indigo/cms/static/sass/partials/cms/theme/",
    ]
)
# Add Purple and White branding to the Learning MFE.
hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-dockerfile-pre-npm-build-learning",
        """
RUN cat >> /openedx/app/src/index.scss <<'PURPLE_THEME_EOF'

/* Custom Purple and White Theme */
:root {
    --primary: #6C3FC5;
    --brand: #6C3FC5;
    --secondary: #F0EAFB;
}

.site-header-desktop .secondary-menu-container .nav-link:focus,
.site-header-desktop .secondary-menu-container .nav-link:hover,
.site-header-desktop .main-nav .nav-link.active,
.site-header-desktop .main-nav .nav-link:focus,
.site-header-desktop .main-nav .nav-link:hover {
    background-color: #6C3FC5 !important;
    color: #FFFFFF !important;
}

.site-header-desktop .main-nav .menu-content {
    border-top-color: #6C3FC5 !important;
}

.nav-underline-tabs .nav-link.active,
.nav-underline-tabs .nav-link:focus,
.nav-underline-tabs .nav-link:hover {
    border-bottom-color: #6C3FC5 !important;
    color: #6C3FC5 !important;
}

.sequence-navigation .btn.active:after {
    background-color: #6C3FC5 !important;
}

.sequence-navigation .sequence-navigation-dropdown .dropdown-menu .btn.active .unit-icon {
    color: #6C3FC5 !important;
}

div.bg-primary.text-white {
    background-color: #6C3FC5 !important;
}

a.brand-link,
a.muted-link {
    color: #6C3FC5 !important;
}

PURPLE_THEME_EOF
        """
    )
)
