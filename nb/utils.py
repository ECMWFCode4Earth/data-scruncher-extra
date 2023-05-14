import subprocess
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def save2ncdf(ds, ds_bitrounded, suffix: 'str' = '') -> None:
    """
    Save dataset in NetCDF format
    """

    ds_bitrounded.to_compressed_netcdf(f"bitrounded_compressed{suffix}.nc")
    ds.to_compressed_netcdf(f"compressed{suffix}.nc")
    ds.to_netcdf(f"original{suffix}.nc")


def save2zarr(ds, ds_bitrounded, suffix: 'str' = '') -> None:
    """
    Save dataset in Zarr format
    """

    ds_bitrounded.to_compressed_zarr(f"bitrounded_compressed{suffix}.zarr",
                                     mode="w")
    ds.to_compressed_zarr(f"compressed{suffix}.zarr", mode="w")
    ds.to_zarr(
        f"original{suffix}.zarr", mode="w",
        encoding={v: {"compressor": None} for v in ds.data_vars}
    )


def hsize(size: int, decimal_places: int = 2) -> str:
    """
    Size from bytes to human readable
    """
    for unit in ['B', 'K', 'M', 'G', 'T', 'P']:
        if size < 1024.0 or unit == 'P':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def get_size(ext: str, suffix: 'str' = '') -> dict:
    """
    Get size of files
    """

    sizes = subprocess.check_output(f'du -s *{suffix}.{ext}',
                                    shell=True).decode("utf-8")

    sizes = sizes.replace('\t', ';').replace('\n', ';').split(';')

    shortnm = {
        f'bitrounded_compressed{suffix}.zarr': 'bitr_comp',
        f'compressed{suffix}.zarr': 'comp', f'original{suffix}.zarr': 'ori',
        f'bitrounded_compressed{suffix}.nc': 'bitr_comp',
        f'compressed{suffix}.nc': 'comp', f'original{suffix}.nc': 'ori',
    }

    output = {}
    for i in range(0, len(sizes)-1, 2):
        output[sizes[i + 1]] = int(sizes[i])

    for k in output.keys():
        output[shortnm[k]] = output.pop(k)

    return output


def get_ratio(data: dict) -> dict:
    """
    Get ratio of sizes
    """

    original = data['ori']

    ratios = {}

    for k in data.keys():
        ratios[k] = np.round(original / data[k])

    return ratios


def plot_ratio(df, type_: str) -> None:
    """
    Plot ratio of sizes
    """
    sns.set_style('dark')

    types = ['ncdf', 'zarr']
    assert type_ in types, f"'{type_}' is not in {types}"

    # plt.yscale('log')

    plt.figure(figsize=(6, 6))
    bar = plt.bar(df.index, df[f'{type_}'].values, alpha=.8)

    # TODO barh!

    # plt.xlabel('Compression Method')
    plt.ylabel('Size in Bytes')
    plt.title(f'{type_} Compression Comparison')

    for rect, lbl in zip(bar, get_ratio(df[f'{type_}']).values()):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'X {int(lbl)}',
                 ha='center', va='bottom', fontsize='medium',
                 fontweight='heavy', c='darkblue')

    plt.tight_layout()
    plt.show()
